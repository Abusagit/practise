names = {}
with open('dataset_3363_4.txt', 'r', encoding='utf-8') as file:
    with open('answer.txt', 'w') as file2:
        for human in file:
            human = human.strip().split(';')
            score = [int(i) for i in human[1:]]
            names[human[0]] = score
            file2.write(str(sum(score) / 3) + '\n')
        mean = []
        for subject in range(len(score)):
            for key in names:
                mean.append(names[key][subject])
            file2.write(str(sum(mean) / len(names)) + ' ')
            mean = []