import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3 (3).txt', 'r') as file:
    adr = file.readline().strip()
m = requests.get(adr).text
print(type(m))
#test = url + r
get = requests.get(url + m).text
while 1:
    adr = requests.get(url + get)
    if adr.text.split()[0] == 'We':
        with open('answer.txt', 'w') as file:
            file.write(adr.text)
        break
    else:
        get = adr.text
        print(get)
print('Ready!')