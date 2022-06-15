import requests
import random

a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)
color = f"{a}, {b}, {c}"
r = requests.get(f"https://www.thecolorapi.com/id?rgb={color}")
colorname = r.json()["name"]['value']

print(f"Your color's rgb value is: R:{a},G:{b},B:{c}")
print(f"Your color's name is: {colorname}")