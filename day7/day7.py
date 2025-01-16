import requests
from cookies import cookie, day7
import re
from itertools import product

url = day7
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)

OPERATORS = ['+', '*']
calibration_result = 0


def split_and_make_list(contents):
    list_of_list = []
    for item in contents:
        list_of_list.append(re.findall(r"\d+", item))
    return list_of_list


def evaluate_left_to_right(numbers, ops):
    result = int(numbers[0])
    for i, op in enumerate(ops):
        if op == '+':
            result += int(numbers[i + 1])
        elif op == '*':
            result *= int(numbers[i + 1])
    return result


def find_valid_equation(numbers, target):
    operator_combinations = product(OPERATORS, repeat=len(numbers) - 1)
    for ops in operator_combinations:
        result = evaluate_left_to_right(numbers, ops)
        if result == target:
            print(
                f"Valid configuration found: {numbers[0]} {' '.join(f'{ops[i]} {numbers[i + 1]}' for i in range(len(ops)))}")
            return True
    return False


if r.status_code == 200:
    content = r.text.splitlines()
    equations = split_and_make_list(content)

    for elem in equations:
        total_value = int(elem[0])
        numbers = elem[1:]

        if find_valid_equation(numbers, total_value):
            calibration_result += total_value
            print(calibration_result)
