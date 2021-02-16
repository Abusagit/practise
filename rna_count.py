rna = set()
while True:
    n = input()
    if n == 'stop':
        break
    else:
        rna.add(n)
print(f'there are {len(rna)} RNAs in review')