import sys


def solver(l, seq, output_number='', filename=sys.stdin):
    states_decoded = {}
    states_per_position = [None for _ in range(l)]
    state = 0
    for i in range(l):
        cur_state = ''.join(line[i] for line in seq)
        if cur_state in states_decoded:
            states_per_position[i] = states_decoded[cur_state]
        else:
            state += 1
            states_decoded[cur_state] = state
            states_per_position[i] = state
    outputer(state, states_per_position, output_number=output_number, filename=filename)


def outputer(state, states_pos, output_number='', filename=sys.stdin):
    if filename == sys.stdin:
        print(state)
        print(*states_pos)
    else:
        # states_pos = ' '.join(map(str, states_pos))
        with open(f"{__file__}{output_number}.txt", 'a') as fw:
            fw.write(f'{state}\n{states_pos}\n')


if __name__ == '__main__':
    # with open('./1/2.txt', 'r') as f_read:
    #     t = int(f_read.readline().strip())
    #     for _ in range(t):
    #         n, l = map(int, f_read.readline().strip().split())
    #         sequences = tuple(f_read.readline().strip() for _ in range(n))
    #         solver(l, sequences, output_number=3, filename=1)
    #         del sequences
    # print('DONE!')
    with open('./1/markers.py2.txt') as f1, open('./1/markers.py3.txt') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(line1)
                print(line1)
                break
        else:
            print('TOTAL IDENTITY')
