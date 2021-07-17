import itertools
import heapq
import numpy as np
from DSA.structures import balancedTree as Tree

# class MassTree(Tree.AVLTree):
#     def find_closest(self, signal):
#         contains = signal in self
#         if contains:
#
#         else:
#             self.put(key=signal, val=signal)
#             # TODO
#             self.delete(signal)
#
#     return result

i = 1


def annotate(combinations, masses, adducts, signals, test_number=0):
    global i
    with open(f'Test_{test_number}.txt', 'a') as f_write:
        # combinations_ = itertools.product(range(m), range(k))
        # my_tree = MassTree()
        # for index_i, index_j in combinations_:
        #     my_tree.put(key=masses[index_i] + adducts[index_j], val=(index_j, index_j))
        # for signal in signals:
        #     closest = my_tree.find_closest(signal)
        #     pass
        for signal in signals:
            combinations +=

            i += 1


if __name__ == '__main__':
    file = input()
    with open(f'{file}.txt', 'r') as f_read:
        t = int(f_read.readline().strip())
        for _ in range(t):
            m_, k_, n_ = map(int, f_read.readline().strip().split())

            masses_ = np.array([float(x) for x in f_read.readline().strip().split()])
            print(f"Masses {t + 1} done")
            adducts_ = np.array([[float(x) for x in f_read.readline().strip().split()]])
            print(f"Adducts {t + 1} done")
            signals_ = np.array([[float(x) for x in f_read.readline().strip().split()]])
            print(f"Signals {t + 1} done")
            # combinations_ = [(index_i, index_j) for index_i, index_j in itertools.product(range(m_), range(k_))
            #                  if masses_[index_i] + adducts_[index_j] > 0]
            combinations_ = masses_ * adducts_.T  # TODO this is wrong - it multiplies, not sum
            print(combinations_)
            print(f"Combinations {t + 1} done")
            annotate(combinations_, masses_, adducts_, signals_, test_number=int(file))
            print(f"Test {_ + 1} done......")

    print('DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

