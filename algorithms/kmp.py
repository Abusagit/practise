
def prefix(s:str) -> list:
    """
    Creates prefix function for KMP algorithm
    """
    P = [0 for _ in range(len(s))]
    i, j = 0, 1
    while j < len(s):
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        # s[i] != s[j]
        elif i: # i > 0
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return P


def kmp(string, substring):
    """
    Performs KMP search
    """
    sub_len = len(substring)
    str_len = len(string)
    if not str_len or sub_len > str_len:
        return None
    P = prefix(substring)
    print(f'>>> {P}')
    entries = []
    i = j = 0
    while i < str_len and j < sub_len:
        if string[i] == substring[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        # string[i] != substring[j]:
        elif j:  # j > 0
            j = P[j - 1]
        else:
            i += 1
    return entries


def kmp_with_crossed_entries(string, substring, symbol='@'):
    """
    Performs KMP search with crossing entries
    """
    entries = []
    mega = substring + symbol + string
    length = len(mega)
    P = [0 for _ in range(length)]
    i, j = 0, 1
    while j < length:
        if mega[i] == mega[j]:
            P[j] = i + 1
            if P[j] == len(substring):
                entries.append(j - 2 * len(substring))
            j += 1
            i += 1
        elif i:
            i = P[i - 1]
        else:
            P[j] = 0
            j += 1
    return entries

if __name__ == '__main__':
    g = '1'
    f = 'asdadsasd'
    print(kmp(f, g))
    # print(prefix('AABAA'))
    s = 'aabaabaaaabaabaaab'
    sub = 'aabaa'
    # print(kmp(s, sub))


    # print(kmp_with_crossed_entries(s, sub))