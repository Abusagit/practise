import numpy as np
from math import log, ceil

char_to_num = dict(zip("ACGTacgtNnx", (0, 1, 2, 3, 0, 1, 2, 3, 99, 99, 99)))  # if IUPAC?????
complement = dict(zip((0, 1, 2, 3), (3, 2, 1, 0)))


def default_l(sequence_length):
    return ceil(1 + log(sequence_length, 4))


"""
void usage() 
{
    fprintf(stderr, "RepeatScout Version %s\n\nUsage: \n"
           "RepeatScout -sequence <seq> -output <out> -freq <freq> -l <l> [opts]\n"
           "     -L # size of region to extend left or right (10000) \n"
           "     -match # reward for a match (+1)  \n"
           "     -mismatch # penalty for a mismatch (-1) \n"
           "     -gap  # penalty for a gap (-5)\n"
           "     -maxgap # maximum number of gaps allowed (5) \n"
           "     -maxoccurrences # cap on the number of sequences to align (10,000) \n"
           "     -maxrepeats # stop work after reporting this number of repeats (10000)\n"
           "     -cappenalty # cap on penalty for exiting alignment of a sequence (-20)\n"
           "     -tandemdist # of bases that must intervene between two l-mers for both to be counted (500)\n"
           "     -minthresh # stop if fewer than this number of l-mers are found in the seeding phase (3)\n"
           "     -minimprovement # amount that a the alignment needs to improve each step to be considered progress (3)\n"
           "     -stopafter # stop the alignment after this number of no-progress columns (100)\n"
           "     -goodlength # minimum required length for a sequence to be reported (50)\n"
           "     -maxentropy # entropy (complexity) threshold for an l-mer to be considered (-.7)\n"
    "    -v[v[v[v]]] How verbose do you want it to be?  -vvvv is super-verbose.\n"
"""

PADLENGTH = 11000  # /* should be >= L+MAXOFFSET */
small_l = 6
SEEDMISMATCHES = 0
HASH_SIZE = 16000057
SMALL_HASH_SIZE = 5003
MINTHRESH = 50  # at end, remove l-mers with freq < MINTHRESH
TANDEMDIST = 30  # l-mers must be this far apart to avoid tandem repeats
MAXN = 10000  # max #occ of lmer (10000)
MAXR = 100000  # max #families (100000)

L = 1000  # size of region to extend left or right (10000)

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
l = default_l(length)


def lmer_match_either(lmer_1, lmer_2):  # forward or rev comp match
    for i in range(l):
        if lmer_1[i] != lmer_2[i]:
            return lmer_match_either(lmer_1, lmer_2)

    return True


def lmer_match_rc(lmer_1, lmer_2):  # rev comp match
    for i in range(l):
        if lmer_1 + lmer_2[l - i - 1] != 3:
            return False
    return True


def mismatches(lmer_1, lmer_2):
    return sum(list(map(lambda x: x[0] != x[1], zip(lmer_1, lmer_2))))  # TODO numpy


def is_degenerate(this):
    pass


def build_headtpr():
    pass


def build_sequence(sequence_, SEQ_FILE):
    boundariesSize = 100
    boundaries = [0 for _ in range(boundariesSize)]
    with open(SEQ_FILE) as f_read:
        for i in range(PADLENGTH):
            sequence_[i] = 99

        i = seq = 0

        for char in file.read():
            if char in {"\n", ">"}:
                continue
            # for j in range(): # TODO


def extend_right():
    def compute_score_right(y, n, offset, best_a):
        nonlocal temp_score
        """
          //RMH: Sequence boundaries check.
          //      bStart                  bEnd
          //    inclusive---------------exclusive
        """
        base_start = PADLENGTH

        if upperBoundI[n] > 0:
            base_start = boundaries[upperBoundI[n] - 1] + PADLENGTH

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
            if a == complement(sequence[pos[n] - (offset + y - L - l) - 1]):
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
                    if a == complement(sequence[pos[n] - (x + y - L - l) - 1]):
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


filepath = "None"
with open(file="None") as file:
    maxlen = len(file.read())

    sequence = [None for _ in range(2 * maxlen + 3 * PADLENGTH)]

removed = sequence.copy()

"""
co_get_int(argc, argv, "-L", &L)                           || (L=10000);
  co_get_int(argc, argv, "-match", &MATCH)                   || (MATCH=1);
  co_get_int(argc, argv, "-mismatch", &MISMATCH)             || (MISMATCH=-1);
  co_get_int(argc, argv, "-gap", &GAP)                       || (GAP=-5);
  co_get_int(argc, argv, "-maxgap", &MAXOFFSET)              || (MAXOFFSET=5);
  co_get_int(argc, argv, "-maxoccurrences", &MAXN)           || (MAXN = 10000);
  co_get_int(argc, argv, "-maxrepeats", &MAXR)               || (MAXR = 100000);
  co_get_int(argc, argv, "-cappenalty", &CAPPENALTY)         || (CAPPENALTY=-20);
  co_get_int(argc, argv, "-minimprovement", &MINIMPROVEMENT) || (MINIMPROVEMENT=3);
  co_get_int(argc, argv, "-stopafter", &WHEN_TO_STOP)        || (WHEN_TO_STOP=100);
  co_get_float(argc, argv, "-maxentropy", &MAXENTROPY)       || (MAXENTROPY=-0.7);
  co_get_int(argc, argv, "-goodlength", &GOODLENGTH)         || (GOODLENGTH=50);
  co_get_int(argc, argv, "-tandemdist", &TANDEMDIST)         || (TANDEMDIST=500);
  co_get_int(argc, argv, "-minthresh", &MINTHRESH)           || (MINTHRESH=3);
"""

score = [[[0 for i in range(-MAXOFFSET, MAXOFFSET + 1)] for j in range(MAXN)] for k in range(2)]

score_of_besty = [[_ for _ in range(2 * MAXOFFSET + 1)] for n in range(MAXN)]  # ?????
rev = [[0 for _ in range(MAXN)]]
upperBoundI = [0 for _ in range(MAXN)]
best_bestscore = [0 for _ in range(MAXN)]  # EXACTLY??
save_best_score = [0 for _ in range(MAXN)]
pos = [0 for _ in range(MAXN)]

masters = [[_ for _ in range(MAXR)] for _ in range(2 * L + l)]  # TODO allocate dynamically

master = [None for _ in range(2 * L + l + 1)]  # master = (char *)malloc( (2*L+l+1) * sizeof(char));   master[2*L+l] # = (char)NULL;
masters_allocated = master.copy()
master_end = master.copy()


length = build_sequence(sequence, SEQ_FILE=None)  # TODO WHAT IS IT
for x in range(length):
    removed[x] = 0

allocate_space()  # TODO Do i need it?
print("Done allocating headptr")
build_headptr(headptr)
print("Done building headptr")

R = 0
prev_best_freq = 1000000000
prev_best_hash = 0

while True:
    best_tmp = find_best_tmp(headptr)
    if best_tmp < MINTHRESH:
        print(f"Stopped at {R} since no more frequent l-mers")
        break

    for x in range(l):
        master[L + x] = sequence[best_tmp] # TODO sequence[(besttmp->lastocc)+x]

    build_pos(best_tmp)  # computes N

    if N < MINTHRESH:
        print(f"N ({N}) is less then MINTHRESH yet ({MINTHRESH})")
        """
      for(x=0; x<l; x++) 
         printf("%c", num_to_char( sequence[(besttmp->lastocc)+x] ) );
      printf("\nh = %d\n", prevbesthash );
      besttmp->freq = N;
      continue;
      """

    if masters_allocated[R] == 0:
        masters_allocated[R] = 1

    extend_right()
    extend_left()

    R += 1
    if R == MAXR:
        break

    mask_tandem(headptr)