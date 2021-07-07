d = {str(key): [] for key in range(1, 12)}
with open('', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines)
    print(type(lines))
    for i in range(len(lines)):
        line = lines[i].strip().split('\t')
        print(line)
        d[line[0]] += [int(line[2])]
print(d)
with open('', 'w') as file:
    for key in d:
        if len(d[key]) == 0:
            file.write(key + ' -' + '\n')
        else:
            file.write(key + ' ' + str(sum(d[key])/len(d[key])) + '\n')
with open('', 'r') as file:
    print(file.read())