import requests
import json

"""Numbers"""


def interest(x):
    # params = {
    #     'number': x,
    #     'type': 'math?json=true'
    # }
    res = requests.get(api_url.format(x))
    # print(res.status_code)
    # print(res.headers['Content-Type'])
    # print(res.text)
    # print(json.loads(res.text))
    # print(type(json.loads(res.text)))
    if json.loads(res.text)['found']:
        return 'Interesting'
    return 'Boring'


# with open('dataset_24476_3 (2).txt', 'r') as numbers:
#     numbers = numbers.readlines()  # numbers - числа, которые нужно проверить ("число\n")
#
# api_url = "http://numbersapi.com/{}/math?json=true"
#
# for number in numbers:
#     print(interest(int(number.strip())))

# """Open Weather Map"""
# city = input('City?')
# api_url = 'https://api.openweathermap.org/data/2.5/weather'
#
# params = {
#     'q': city, #'Saint Petersburg',
#     'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
#     'units': 'metric'
#
# }
#
# res = requests.get(api_url, params = params)
# #print(res.status_code)
# #print(res.headers['Content-Type'])
# #print(res.json())
# data = res.json()
# template = 'Current temperature in {} is {}'
# print(template.format (city, data['main']['temp']))


"""Artsy.Net"""

client_id = 'fce94574d9751134667b'
client_secret = '9ca947de4ec38a612ec37edb4e50ea95'


def response():
    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      }
                      )

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    token = j["token"]
    # print(token)
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    with open('dataset_24476_4 (1).txt', 'r') as file:
        file = file.readlines()
        # print(file)
        birthdays = []
        names = []
        for line in file:
            r = requests.get("https://api.artsy.net/api/artists/{}".format(line.strip()), headers=headers)
            r.encoding = 'utf-8'
            # print(line)
            j = json.loads(r.text)
            # print(j['sortable_name'], j['birthday'], sep=' <---- ')
            names.append(j['sortable_name'])
            birthdays.append(j['birthday'])
        return {name: int(birthday) for (name, birthday) in zip(names, birthdays)}


sorted_artists = sorted(response().items(), key=lambda x: (x[1], x[0]))
with open('artists.txt', 'w', encoding='utf-8') as file:
    for artist in sorted_artists:
        file.write(artist[0] + '\n')
