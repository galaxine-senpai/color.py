import requests
import random

a = random.randint(0,255) #Red.
b = random.randint(0,255) #Green.
c = random.randint(0,255) #Blue.
color = f"{a}, {b}, {c}" #RGB values all together.
r = requests.get(f"https://www.thecolorapi.com/id?rgb={color}")

print("Name: " + r.json()["name"]['value']) #Prints the name
print("Hex: " + r.json()["hex"]["value"]) #Prints the hex code
print(f"Red: {a}, Green: {b}, Blue: {c}") #Prints the RGB values
print("Image: " + r.json()["image"]["named"]) #Prints the link to the image
