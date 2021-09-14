import sys


def count_price(string) -> int:
    left = 0
    right = len(string) - 1
    price = 0
    while left < right:
        price += string[left] != string[right]
        left += 1
        right -= 1
    return price


s = sys.stdin.readline().strip()
print(count_price(s))

assert count_price("a") == 0, f"{count_price('a')}"
assert count_price("ab") == 1, f"{count_price('ab')}"
assert count_price("cognitive") == 4, f"{count_price('cognitive')}"
assert count_price("aba") == 0, f"{count_price('aba')}"