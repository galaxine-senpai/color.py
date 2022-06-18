#|------------------------------------------------------------------------------------------------|#imports
import requests
import random
import pyfiglet
#|------------------------------------------------------------------------------------------------|#definitons
red = random.randint(0,255) #Red.
blue = random.randint(0,255) #Green.
green = random.randint(0,255) #Blue.
color = f"{red},{blue},{green}" #RGB values all together.
r = requests.get(f"https://www.thecolorapi.com/id?rgb={color}")
banner = ascii_banner = pyfiglet.figlet_format("Color.py")
author = ascii_banner = pyfiglet.figlet_format("By: gawaxine.exe")
#|------------------------------------------------------------------------------------------------|#actual code
print(banner)
print("------------------------------------------------------------------------------------------------")
print(author)
print("------------------------------------------------------------------------------------------------")
print("(Closest color) name: " + r.json()["name"]['value']) #Prints the name
print("------------------------------------------------------------------------------------------------")
print("Is actual color name: " + r.json()["name"]["exact_match_name"]) #This will be false 99% of the time from testing
print("------------------------------------------------------------------------------------------------")
print("Hex: " + r.json()["hex"]["value"]) #Prints the hex code
print("------------------------------------------------------------------------------------------------")
print(f"Red: {red}, Green: {blue}, Blue: {green}") #Prints the RGB values
print("------------------------------------------------------------------------------------------------")
print("HSV: " + r.json()["hsv"]["value"]) #Prints the HSV value
print("------------------------------------------------------------------------------------------------")
print("Image: " + r.json()["image"]["named"]) #Prints the link to the image
print("------------------------------------------------------------------------------------------------")
print("Image: " + r.json()["image"]["named"]) #Prints the link to the image
print("------------------------------------------------------------------------------------------------")
