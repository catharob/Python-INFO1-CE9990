"""
inout.py

Here is a program that will do some stuff. 
"""

import sys

try:
    s = input("How many strawberries would you like in your smoothie? ")
except EOFError:
    print("Ten is a reasonable number.")
    s = "10"

try:
    s = int(s)
except ValueError:
    print("Ten is a reasonable number.")
    s = 10

try:
    ba = input("How many bananas would you like in your smoothie? ")
except EOFError:
    print("One is probably fine.")
    ba = "1"

try:
    ba = int(ba)
except ValueError:
    print("One is probably fine.")
    ba = 1

try:
    bl = input("How many blueberries would you like in your smoothie? ")
except EOFError:
    print("Fifty okay? Sure.")
    bl = "50"

try:
    bl = int(bl)
except ValueError:
    print("Fifty okay?")
    bl = 50

strawCal = 4*s
strawWeight = 10.91*s
bananaCal = 105*ba
bananaWeight = 118*ba
blueCal = 0.78*bl
blueWeight = 1.36*bl
milkCal = 317
milkWeight = 64

allCal = int(round(strawCal + bananaCal + blueCal + milkCal, 0))
allWeight = strawWeight + bananaWeight + blueWeight + milkWeight
allOz = round(allWeight*.035, 2)

print("Let's add half a cup of milk.")
print("Your smoothie contains", s, "strawberries,", ba, "bananas,", bl, "blueberries, and milk.")
print("That's a", allCal, "calorie smoothie. It's about", allOz, "ounces.")

sys.exit(0)
