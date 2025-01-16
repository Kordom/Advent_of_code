
import requests

from cookies import cookie, day1

url = day1
cookies = {
    'session': cookie
}


r = requests.get(url,cookies=cookies)

list1 = []
list2 = []
distance = []

if r.status_code == 200:
    content = r.text.splitlines()
    for elem in content:
        items = elem.split()
        list1.append(int(items[0]))
        list2.append(int(items[1]))

    for i in range(len(list1)):
        min_number_in_list1 = min(list1)
        min_number_index = list1.index(min_number_in_list1)

        min_number_in_list2 = min(list2)
        min_number_index2 = list2.index(min_number_in_list2)

        if min_number_in_list1 > min_number_in_list2:
            distance_value = min_number_in_list1 - min_number_in_list2
            distance.append(distance_value)
            list1.pop(min_number_index)
            list2.pop(min_number_index2)
        else:
            distance_value = min_number_in_list2 - min_number_in_list1
            distance.append(distance_value)
            list1.pop(min_number_index)
            list2.pop(min_number_index2)

    print(sum(distance))
else:
    print('None')




