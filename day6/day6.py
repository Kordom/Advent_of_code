import requests
from cookies import cookie, day6

url = day6
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)

if r.status_code == 200:
    content = r.text.splitlines()
    guard_coordinates = []

    moves = []
    moving_up = True
    moving_down = None
    moving_left = None
    moving_right = None

    # finding guard
    for elem in content:
        if "^" in elem:
            guard_coordinates.append(content.index(elem))
            for i in elem:
                if i == "^":
                    guard_coordinates.append(elem.index(i))

    while True:
        try:
            moves.append(guard_coordinates.copy())
            next_move_right = content[guard_coordinates[0]][guard_coordinates[1] + 1]
            next_move_left = content[guard_coordinates[0]][guard_coordinates[1] - 1]
            next_move_up = content[guard_coordinates[0] - 1][guard_coordinates[1]]
            next_move_down = content[guard_coordinates[0] + 1][guard_coordinates[1]]
        except IndexError:
            unique_items = set(tuple(sublist) for sublist in moves)
            print(len(unique_items))
            break

        if next_move_up != "#" and moving_up:
            guard_coordinates[0] = guard_coordinates[0] - 1
            print(guard_coordinates)
        elif next_move_right != "#" and moving_right:
            guard_coordinates[1] = guard_coordinates[1] + 1

            print(guard_coordinates)
        elif next_move_down != "#" and moving_down:
            guard_coordinates[0] = guard_coordinates[0] + 1

            print(guard_coordinates)
        elif next_move_left != "#" and moving_left:
            guard_coordinates[1] = guard_coordinates[1] - 1
            print(guard_coordinates)

        if next_move_up == "#" and moving_up:
            moving_up = False
            moving_down = False
            moving_left = False
            moving_right = True
        elif next_move_right == "#" and moving_right:
            moving_up = False
            moving_down = True
            moving_left = False
            moving_right = False
        elif next_move_down == "#" and moving_down:
            moving_up = False
            moving_down = False
            moving_left = True
            moving_right = False

        elif next_move_left == "#" and moving_left:
            moving_up = True
            moving_down = False
            moving_left = False
            moving_right = False
















