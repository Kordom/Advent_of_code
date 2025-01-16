import requests
from cookies import cookie

url = "https://adventofcode.com/2024/day/5/input"
cookies = {
    'session': cookie
}

r = requests.get(url, cookies=cookies)
