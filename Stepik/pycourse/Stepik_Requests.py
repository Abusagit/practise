import requests
with open('dataset_3378_3.txt', 'r') as file:
    adr = file.read()
    print()
print(type(adr))
L = adr.splitlines()
print(L)
n = len(L)
print(n)
with open('answer.txt', 'w') as file:
    file.write(str(n))