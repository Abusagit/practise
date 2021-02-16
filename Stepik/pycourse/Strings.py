s, a, b = (input() for _ in range(3))


def operations(string, find, insert, count=1):
    if find not in string and count == 1:
        return 0
    if find in insert and find in insert:
        return "Impossible"
    string = string.replace(find, insert)
    if find in string:
        count += 1
        return operations(string, find, insert, count)
    return count


print(operations(s, a, b))


s, t = (input() for _ in range(2))
count = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        count += 1
print(count)