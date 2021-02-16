s, d, m, w = str(), dict(), 0, str()
with open("dataset_3378_3.txt", "r", encoding='utf-8') as file:
    s = file.read().lower().strip().split()
print(s)
s.sort()
print(type(s))
print(s)
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word
print(d)
print(w, m, end=' ')