import requests
from cookies import cookie, day9

url = day9
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)


def make_disk_map(cont):
    id_counter = 0
    id_number_block = []

    for i, block in enumerate(cont):
        if i % 2 == 0:
            for _ in range(int(block) + 1):
                id_number_block.append(id_counter)
            id_counter += 1
        else:
            if int(block) == 0:
                continue
            for _ in range(int(block) + 1):
                id_number_block.append(".")
    return id_number_block


def search_number_from_end(diskmap, last_id):
    i = last_id

    while True:
        i -= 1
        value = diskmap[i]
        if value == ".":
            continue
        else:
            # print(value, i)
            yield value, i


def arrange_file_blocks(diskmap):
    crawler = -1
    last_id = 0
    dot_count = diskmap.count('.')
    print(dot_count)
    arranged_file = diskmap.copy()
    for elem in diskmap:
        if last_id == -(dot_count-1):
            break
        crawler += 1
        if elem == ".":
            number = search_number_from_end(arranged_file, last_id)
            unpacked_number = next(number)
            temp = arranged_file[crawler]
            arranged_file[crawler] = unpacked_number[0]
            arranged_file[unpacked_number[1]] = temp
            last_id = unpacked_number[1]
            # print(arranged_file)
        else:
            continue
    return arranged_file


# def move_file_blocks(diskmap):
#     compacted_file = diskmap.copy()
#     start_from_back = 0
#     start_from_front = -1
#     for i in diskmap:
#         start_from_front += 1
#         if i.isnumeric():
#             continue
#         else:
#             for number in compacted_file[::-1]:
#                 start_from_back -= 1
#                 if number.isnumeric():
#                     break
#             temp = compacted_file[start_from_front]
#             compacted_file[start_from_front] = compacted_file[start_from_back]
#             compacted_file[start_from_back] = temp
#             print(compacted_file)
#     return compacted_file

# def move_file_blocks(diskmap):
#     compacted_file = diskmap.copy()
#     start_from_back = 0
#     start_from_front = -1
#     generator_forward = (number for number in diskmap)
#     generator_backward = (number for number in diskmap[::-1])
#
#     for _ in diskmap:
#         if start_from_back == ((-start_from_front + 2) / 2) and start_from_front != -1 and start_from_back != 0:
#             break
#         forward_number = next(generator_forward)
#         start_from_front += 1
#         if forward_number.isnumeric():
#             continue
#         else:
#             for _ in range(1000):
#                 backward_number = next(generator_backward)
#                 start_from_back -= 1
#                 if backward_number.isnumeric():
#                     temp = compacted_file[start_from_front]
#                     compacted_file[start_from_front] = compacted_file[start_from_back]
#                     compacted_file[start_from_back] = temp
#                     break
#
#         print(compacted_file)
#     return compacted_file


if r.status_code == 200:
    content = "".join(r.text.splitlines())
    # content = "2333133121414131402"
    disk_map = make_disk_map(content)
    # print(disk_map)
    print(arrange_file_blocks(disk_map))

