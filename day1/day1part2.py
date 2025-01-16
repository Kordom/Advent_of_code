import requests


from cookies import cookie, day2

url = day2
cookies = {
    'session': cookie
}


r = requests.get(url,cookies=cookies)

list1 = []
list2 = []
similarity = []

if r.status_code == 200:
    content = r.text.splitlines()
    for elem in content:
        items = elem.split()
        list1.append(items[0])
        list2.append(items[1])

    for elem in list1:
        occur = list2.count(elem)
        ans = int(elem) * int(occur)
        similarity.append(ans)
else:
    print('None')

print(sum(similarity))



