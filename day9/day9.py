import requests
from cookies import cookie, day9

url = day9
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)

def make_disk_map(content):
    id_counter = 0
    id_number_block = ""

    for i, block in enumerate(content):
        if i % 2 == 0:
            id_number_block += int(block) * str(id_counter)
            id_counter += 1
        elif block == "\n" or block == 0:
            continue
        else:
            id_number_block += int(block) * "."
    return id_number_block


if r.status_code == 200:
    content = r.text

    disk_map = make_disk_map(content)
    print(disk_map)






    # for i in range(len(content)):
    #     print(i)


