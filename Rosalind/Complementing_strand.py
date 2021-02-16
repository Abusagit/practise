def complement(dna):
    code = {
        'A':'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    res = ''
    for i in range(len(dna)-1, -1, -1):
        res += code[dna[i]]
    return res


if __name__ == '__main__':
    class FunctionError(Exception):
        pass


    s = 'AAAACCCGGT'
    s_c = complement(s)
    assert s_c == 'ACCGGGTTTT', FunctionError
    f = input()
    print(complement(f))
