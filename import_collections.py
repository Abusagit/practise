import collections

cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

c = collections.Counter({'red': 4, 'blue': 2})
print(c)
c = collections.Counter(cats=4, dogs=8)
print(c)