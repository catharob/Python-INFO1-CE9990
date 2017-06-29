"""
graphpaper.py

Tell me how big you want the squares to be in your graph paper, and how much you'd like of it, and I'll print it out for you.

"""

import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
rSpace = int(input("How many rows of spaces in each box (e.g., 1)? "))
cSpace = int(input("How many columns of spaces in each box (e.g., 3)? "))

r = 1
# c = 1
# rs = 1
# cs = 1

while r <= rows:
	print("\n", end = "")
	rs = 1
	c = 1
	while rs <= rSpace:
		
		while c <= columns:

			print("+", end = "")
			cs = 1
			while cs <= cSpace:
				print("-", end = "")
				cs += 1

			c += 1
			
		print("\n", end = "")
		c = 1
		

		while c <= columns:
			print("|", end = "")
			cs = 1
			while cs <= cSpace:
				print(" ", end = "")
				cs += 1 
			c +=1
			
		rs +=1

	# rs = 1
	# c = 1
	r += 1

sys.exit(0)