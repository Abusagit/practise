def str_widening(x):
    a = ''
    k = ''
    let = ''
    for ind in range(len(x)):
        if ind < len(x) - 1:
            if x[ind].isalpha():
                let = x[ind]
            elif x[ind].isdigit() and x[ind + 1].isdigit():
                k = k + x[ind]
            else:
                a = a + let * int((k + x[ind]))
                k = ''
        else:
            a = a + let * int((k + x[ind]))
    with open('answer.txt', 'w') as file2:
        file2.write(str(a))


with open('dataset_3363_2 (3).txt', 'r') as file:
    for line in file:
        line = line.strip()
        str_widening(line)