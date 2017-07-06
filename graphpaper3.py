"""
graphpaper3.py

Tell me how big you want the squares to be in your graph paper, and how much you'd like of it, and I'll print it out for you.

"""

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rSpace = int(input("How many rows of spaces in each box (e.g., 1)? "))
cSpace = int(input("How many columns of spaces in each box (e.g., 3)? "))

for n in range(rows):
	for j in range(columns):
		print("+", end="")
		for i in range(0, cSpace):
			print("-", end="")

	print()

	for m in range(rSpace):
		for l in range(columns):
			print("|", end="")
			for k in range(0, cSpace):
				print(" ", end="")
		print()


sys.exit(0)