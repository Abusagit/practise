import re
import requests


# a, b = (_ for _ in input().split())
#
# pattern = re.compile(r'https:.*\.html')
# url = requests.get(a)
# links = pattern.findall(url.text)
# answer = []
# for link in links:
#     try:
#         answer.extend(pattern.findall(requests.get(link).text))
#         if b in answer:
#             print('Yes')
#     except requests.exceptions.ConnectionError:
#         continue
# if b not in answer:
#     print('No')

#  составление функции с автоматической проверкой
def check_search(x):
    with open(r'/Stepik/pycourse/requests_right_answer_test.txt', 'r') as file:
        for i in x:
            print((i + '______' + file.readline().strip()) if i != file.readline().strip() else 'Ok')


def web_search_v1(link):
    answer = list()
    site = requests.get(link).text
    sites = sorted(list(set(pattern.findall(site))))
    for found_site in sites:
        answer.append(found_site[1])
    return answer


def web_search_v2(link):
    answer = list()
    site = requests.get(link).text
    sites = sorted(list(set(pattern.findall(site))))
    for found_site in sites:
        answer.append((found_site[1]))
    answer = set(sorted(answer))
    return answer


pattern = re.compile(r"""<a.*href=[\'\"]?([\w\d]+://)?(\w+.*?\w+)[:"'/]""")
"http://pastebin.com/raw/7543p0ns"
if __name__ == '__main__':
    a = input()

    check_search(web_search_v1(a))
    print('Check #1 done')
    check_search(web_search_v2(a))
    print('Check #2 done')
