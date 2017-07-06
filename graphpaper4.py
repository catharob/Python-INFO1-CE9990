"""
graphpaper3.py

Tell me how big you want the squares to be in your graph paper, and how much you'd like of it, and I'll print it out for you.

This version also closes the ends of the graph paper.

(Using functions and for loops, and one while loop.)

"""

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rSpace = int(input("How many rows of spaces in each box (e.g., 1)? "))
cSpace = int(input("How many columns of spaces in each box (e.g., 3)? "))


def makePlusRow(numberOfColumns, spaceInColumns):
	for j in range(numberOfColumns):
		print("+", end="")
		for i in range(spaceInColumns):
			print("-", end="")
	print("+")

def makeBarRow(numberOfColumns, spaceInColumns):
	for l in range(numberOfColumns):
		print("|", end="")
		for k in range(spaceInColumns):
			print(" ", end="")
	print("|")

def makeGraphPaper(numberOfRows, spaceInRows):
	for m in range(numberOfRows):
		makePlusRow(columns, cSpace)
		x = 1
		while x <= spaceInRows:
			makeBarRow(columns, cSpace)
			x +=1
	makePlusRow(columns, cSpace)

makeGraphPaper(rows, rSpace)


sys.exit(0)