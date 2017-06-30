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


def makePlusRow(input1, input2):
	for j in range(0, input1):
		print("+", end="")
		for i in range(0, input2):
			print("-", end="")
	print("+")

def makeBarRow(input1, input2):
	for l in range(0, input1):
		print("|", end="")
		for k in range(0, input2):
			print(" ", end="")
	print("|")

def makeGraphPaper(input3, input4):
	for m in range(0, input3):
		makePlusRow(columns, cSpace)
		x = 1
		while x <= input4:
			makeBarRow(columns, cSpace)
			x +=1
	makePlusRow(columns, cSpace)

makeGraphPaper(rows, rSpace)


sys.exit(0)