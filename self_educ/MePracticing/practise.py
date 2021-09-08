a = 10
def f():
    global a
    a = 20

print(a)
f()
print(a)