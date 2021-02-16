def primers(primer):
    '''calculating primers annealing temperature'''
    a_t = primer.count('A') + primer.count('T')
    g_c = primer.count('G') + primer.count('C')
    return 2 * a_t + 4 * g_c


if __name__ == '__main__':
    q = 'ACCCACACAAAATGATGCCCAG'
    w = 'TGCCCCATTATTTAGCCAGGAG'
    for i in q,w:
        print(primers(i))