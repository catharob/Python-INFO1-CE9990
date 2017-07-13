"""
emilyFileReader.py
Reads a poem and print it out.
"""

import sys

#macOS
filename = "/Users/Catherine/Documents/Python Practice Programs/NYU Class/emily.txt"

try:
    lines = open(filename)
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

for line in lines:
    print(line, end = "")   

# NOTE: trying to turn capital letters into lower case letters (except if first letter of the line) but haven't yet succeeded.
# for line in lines:
# 	for letter in line:
# 		if letter[] == 0 and letter.isupper():
# 			letter.lower()
# 	print(line, end = "")

lines.close()
sys.exit(0)