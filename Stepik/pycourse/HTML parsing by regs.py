import re

import requests

from Stepik.Requests_practise import check_search

pattern = re.compile(r""".*<a.*href=[\'\"]?([\w\d]+://)?(\w+.*?\w+)[:"'/]""")
a = input()
# построчный список строк на сайте:
result = requests.get(a).text.splitlines()

correct_sites = list()
for string in result:
    match = pattern.match(string)
    if match:
        # print(match.groups())
        correct_sites.append(match.group(2))
correct_sites = sorted(list(set(correct_sites)))
print(*correct_sites, sep='\n')

check_search(correct_sites)
