import math
import sys
from os import rename

import requests

name = input("Your Name?")


def greet(who_to_greet):
    return f"Hello, {who_to_greet}!"


print(greet(name))

# r = requests.get("https://github.io")
# print(r.status_code)
