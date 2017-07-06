"""
graphpaper2.py

Tell me how big you want the squares to be in your graph paper, and how much you'd like of it, and I'll print it out for you.

This version also closes the ends of the graph paper.

Now having seen a much simpler version of this program in class, I'm using the string multiplication method rather than the while loop method.

"""

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rSpace = int(input("How many rows of spaces in each box (e.g., 1)? "))
cSpace = int(input("How many columns of spaces in each box (e.g., 3)? "))

tinyPlusUnit = "+" + cSpace*"-"
longPlusLine = columns*tinyPlusUnit + "+\n"

tinyBarUnit = "|" + cSpace*" "
longBarLine = columns*tinyBarUnit + "|\n"

wholeRow = longPlusLine + rSpace*longBarLine

wholeGraphPaper = rows*wholeRow + longPlusLine

print(wholeGraphPaper)



sys.exit(0)