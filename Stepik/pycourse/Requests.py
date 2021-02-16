import requests

# request link:
res = requests.get("https://docs.python.orgaaaaa/3.5/")
# status-code 200 - OK
print(res.status_code)
# print type of content
print(res.headers['Content-Type'])
# get body of resource:  - byte links
print(res.content)
# we can get text if we are sure that content is a text - HTML-content
print(res.text)


# This is an image
res2 = requests.get("https://www.crummy.com/software/BeautifulSoup/10.1.jpg")
print(res2.status_code)
print(res2.headers['Content-Type'])

print(res2.content)

with open("picture.jpg", 'wb') as file:
    file.write(res2.content)


# request to browser:
res = requests.get("https://yandex.ru/search",
                   paramns={
                       'text': 'Stepic',
                       'test': 'test1',
                       'name': 'Name with whitespace',
                       'list': ['test1', 'test2']
                   })
print(res.status_code)
print(res.headers)
print(res.url)