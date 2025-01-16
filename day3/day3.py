from re import match

import requests
import re

from cookies import cookie, day3

url = day3
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)

def multiply_and_add(content):
    overall_sum = 0
    for elem in content:
        list_of_numbers = elem.group(2).split(',')
        previous_number = 0
        for n in list_of_numbers:
            if previous_number == 0:
                previous_number = int(n)
                continue
            overall_sum += previous_number * int(n)
    print(overall_sum)





if r.status_code == 200:
    content = r.text
    matches = re.finditer("(mul[(](\d*[,]\d*)[)])",content)

    multiply_and_add(matches)