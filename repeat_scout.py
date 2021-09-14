import numpy as np
from math import log, ceil


def default_l(length):
    return ceil(1 + log(length, 4))


PADLENGTH = 11000
small_l = 6
SEEDMISMATCHES = 0
HASH_SIZE = 16000057
SMALL_HASH_SIZE = 5003

MINTHRESH = 50  # at end, remove l-mers with freq < MINTHRESH
TANDEMDIST = 30  # l-mers must be this far apart to avoid tandem repeats
MAXN = 10000  # max #occ of lmer (10000)
MAXR = 100000  # max #families (100000)

MATCH = 1
MISMATCH = -1
GAP = -5
CAPPENALTY = -20  # cap on penalty for exiting alignment (-20)
MAXOFFSET = 5
MINIMPROVEMENT = 3  # amount totalbestscore must improve for each extra letter (3) */
WHEN_TO_STOP = 500  # stop if no improvement after extending this far (500)

MAXENTROPY = -0.7  # ignore freq l-mers with entropy greater than this (-0.70)
GOODLENGTH = 50  # minimum length of a good subfamily (50)

length = 213128371920
default_length = default_l(length)

score = [[[0 for i in range(-MAXOFFSET, MAXOFFSET + 1)] for j in range(MAXN)] for k in range(2)]


def extend_right():
    def compute_score_right(y, n, offset, best_a):
        """
          //RMH: Sequence boundaries check.
          //      bStart                  bEnd
          //    inclusive---------------exclusive
        """
        base_start = PADLENGTH

        if upperBoundI[n] > 0:
            base_start = boundaries[upperBound[n] - 1] + PADLENGTH

        base_end = boundaries[upperBoundI[n]] + PADLENGTH

        # ???????????????????
        bStart = 0
        bEnd = 50000000

        if rev[n]:
            if pos[n] - (offset + y - L - l) - 1 < base_start:
                return 0
        else:
            if pos[n] + offset + y - L >= base_end:
                return 0

        ans = -1000000000
        #   /* first, try oldoffset = offset+1.
        #      This means master[y]=a aligns to - */

        if offset < MAXOFFSET:
            old_offset = offset + 1
            temp_score = score[y % 2][n][old_offset + MAXOFFSET] + GAP
            ans = max(temp_score, ans)

        #   /* next, try oldoffset = offset.
        #    This means master[y]=a aligns to sequence[pos[n]+offset+y-L] */

        old_offset = offset
        temp_score = score[(y - 1) % 2][n][old_offset + MAXOFFSET]
        if rev[n]:
            if a == compl(sequence[pos[n] - (offset + y - L - l) - 1]):
                temp_score += MATCH
            else:
                temp_score += MISMATCH;
        else:
            if a == sequence[pos[n] + offset + y - L]:
                temp_score += MATCH
            else:
                temp_score += MISMATCH

        ans = max(ans, temp_score)
        #  /* finally, try oldoffset < offset
        #     This means master[y]=a aligns to one of
        #     sequence[pos[n]+oldoffset+y-L] ... sequence[pos[n]+offset+y-L].
        #     Also, offset-oldoffset gaps */

        for oldoffset in range(-MAXOFFSET, offset):
            is_match = 0
            for x in range(oldoffset, offset):
                if rev[n]:
                    if a == compl(sequence[pos[n] - (x + y - L - l) - 1]):
                        ismatch = 1
                else:
                    if a == sequence[pos[n] + x + y - L]:
                        ismatch = 1
            temp_score = score[(y - 1) % 2][n][oldoffset + MAXOFFSET]
            temp_score += (offset - oldoffset) * GAP
            if ismatch == 1:
                temp_score += MATCH
            else:
                temp_score += MISMATCH

            temp_score = max(temp_score, ans)

        return ans

    def compute_total_best_score_right(y):
        nonlocal best_bestscore
        nrepeat_occ = 0
        n_active_repeat_occ = 0
        total_best_score = 0

        for n in range(N):
            best_score = max(best_bestscore[n] + CAPPENALTY, 0)

            for offset in range(-MAXOFFSET, MAXOFFSET + 1):
                best_score = max(score[y % 2][n][offset + MAXOFFSET], best_score)

            n_repeat_occ += best_score > 0  # if(bestscore > 0) nrepeatocc++
            n_active_repeat_occ += best_score > best_bestscore[
                n] + CAPPENALTY  # if(bestscore > bestbestscore[n] + CAPPENALTY) nactiverepeatocc++
            best_bestscore[n] = max(best_bestscore[n],
                                    best_score)  # if(bestscore > bestbestscore[n]) bestbestscore[n] = bestscore;
            total_best_score += best_score
        if all((total_bestscore >= best_totalbestscore + (y - besty) * MINIMPROVEMENT,
                total_bestscore > best_totalbestscore)):  # * to deal with MINIMPROVEMENT=0
            besty = y
            best_totalbestscore = total_bestscore
            best_n_active_repeat_occ = n_active_repeat_occ

            for n in range(N):
                save_best_score[n] = best_bestscore[n]
                for offset in range(-MAXOFFSET, MAXOFFSET + 1):
                    score_of_besty[n][offset + MAXOFFSET] = score[y % 2][n][offset + MAXOFFSET]

        return None

    best_a = 0
    y = L + l - 1
    for n in range(N):
        for offset in range(-MAXOFFSET, MAXOFFSET + 1):
            score[y % 2][n][offset + MAXOFFSET] = l * MATCH
            if offset < 0:
                score[y % 2][n][offset + MAXOFFSET] += -offset * GAP
            elif offset > 0:
                score[y % 2][n][offset + MAXOFFSET] += offset * GAP
        best_bestscore[n] = l * MATCH

    besty = L + l - 1

    for n in range(N):
        for offset in range(-MAXOFFSET, MAXOFFSET + 1):
            score_of_besty[n][offset + MAXOFFSET] = score[y % 2][n][offset + MAXOFFSET]

    best_totalbestscore = 0
    compute_total_best_score_right(y)  # TODO N * l * MATCH

    for y in range(L + l, 2 * L + l):
        new_totalbestscore = 0

        for a in range(4):
            new_totalbestscore_a = 0
            for n in range(4):
                best_score = max(0, best_bestscore[n] + CAPPENALTY)

                for offset in range(-MAXOFFSET, MAXOFFSET + 1):
                    temp_score = compute_score_right(y, n, offset, a)

                    best_score = max(best_score, temp_score)

                new_totalbestscore_a += best_score

            if new_totalbestscore_a > new_totalbestscore:
                new_totalbestscore = new_totalbestscore_a
                best_a = a
        master[y] = best_a
        for n in range(N):
            for offset in range(-MAXOFFSET, MAXOFFSET + 1):
                score[y % 2][n][offset + MAXOFFSET] = compute_score_right(y, n, offset, best_a)
        compute_total_best_score_right(y)
        if y - besty >= WHEN_TO_STOP:
            break
    y = besty
    total_bestscore = best_totalbestscore
    n_repeat_occ = best_n_repeat_occ
