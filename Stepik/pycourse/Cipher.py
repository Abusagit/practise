import simplecrypt

"""САЙТ: https://pypi.org/project/simple-crypt/"""

string = ''
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", 'r') as file:
    file = file.readlines()
    for i in range(len(file)):
        file[i] = file[i].strip()
print(encrypted)
print(file)
# for password in file:
#     try:
#         x = simplecrypt.decrypt(password, encrypted).decode('utf8') ##ОБЯЗАТЕЛЬНО для кодировки из байтов!!!!
#     except simplecrypt.DecryptionException: ## Ожидание неправильного пароля и продолжение итерации
#         print('%s is Incorrect password' % password)
#     else:
#         print(x, '%s is correct password' % password, sep='\n\n')
#         break

password = 'Asdkh12dasdlhulkra'
y = simplecrypt.encrypt(password, 'Привет')
print(y)

