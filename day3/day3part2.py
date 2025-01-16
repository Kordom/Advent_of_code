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
    mul_instructions = True
    for elem in content:
        print(elem.group(1), elem.group(2), elem.group(4))
        if elem.group(1) is not None:
            mul_instructions = False
            continue
        elif elem.group(2) is not None:
            mul_instructions = True
            continue
        elif mul_instructions:
            if elem.group(4) is not None:
                list_of_numbers = elem.group(4).split(',')
                previous_number = 0
                for n in list_of_numbers:
                    if previous_number == 0:
                        previous_number = int(n)
                        continue
                    overall_sum += previous_number * int(n)
            else:
                continue

    print(overall_sum)


if r.status_code == 200:
    content = r.text
    matches = re.finditer("(don.t[(][)])|(do[(][)])|(mul[(](\d*[,]\d*)[)])",content)

    multiply_and_add(matches)

