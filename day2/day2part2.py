from collections import Counter

import requests

from cookies import cookie, day2

url = day2
cookies = {
    'session': cookie
}


r = requests.get(url, cookies=cookies)

passed_report = 0
passed = None


if r.status_code == 200:
    content = r.text.splitlines()

    for elem in content:
        allowed_mistakes = 1
        cont = elem.split()
        is_increasing = None
        is_decreasing = None
        legit = None
        previous_number = int(0)

        if passed:
            passed_report += 1
            passed = None

        # Checks if the line is increasing or decreasing and breaks if not passing
        for i in cont:
            if (previous_number <= int(i) and is_decreasing) or (previous_number >= int(i) and is_increasing):
                legit = False

                break

            elif previous_number == 0:
                counts = Counter(cont)
                is_repeats = any(num > 1 for num in counts.values())
                if is_repeats:

                    break
                previous_number = int(i)
                continue

            elif previous_number > int(i):
                is_decreasing = True
                legit = True
                previous_number = int(i)
                continue

            elif previous_number < int(i):
                is_increasing = True
                legit = True
                previous_number = int(i)
                continue

        if legit:
            previous_number = 0
            for i in cont:
                if previous_number == 0:
                    previous_number = int(i)
                    continue
                if 1 <= abs(int(i) - previous_number) <= 3:
                    previous_number = int(i)
                    passed = True
                    continue
                else:
                    passed = False

                    break
            if passed:
                passed_report += 1
                passed = None
else:
    print('None')



print(passed_report)

