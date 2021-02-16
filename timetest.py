import timeit
import sys

def to_jaden_case1(string: str) -> str:
    return ' '.join(map(lambda x: x[0].upper() + x[1:], string.split()))

def to_jaden_case2(string):
    return ' '.join([x[0].upper() + x[1:] for x in string.split()])


example = "winston churchill was born at blenheim palace, near woodstock in oxfordshire. winstons father, lord randolph churchill, was a politician. winstons mother, lady randolph churchill of brooklyn, new york, was a daughter of american millionaire leonard jerome. as the son of a prominent politician, it was unsurprising that churchill was soon drawn into politics himself"


# print(timeit.timeit(stmt='to_jaden_case1(example)', number=1000, globals=globals()))
print((timeit.timeit(stmt='to_jaden_case1(example)', number=1, globals=globals())))
print(sys.getsizeof(to_jaden_case1(example)))

# print(timeit.timeit(stmt='to_jaden_case2(example)', number=1000, globals=globals()))
print(timeit.timeit(stmt='to_jaden_case2(example)', number=1, globals=globals()))
print(sys.getsizeof(to_jaden_case2(example)))
print(sys.getsizeof(to_jaden_case1))
print(sys.getsizeof(example))