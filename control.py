"""
control.py

This program asks for your favorite horror movie and then offers some custom advice.

"""

import sys

print(
"""
What's your favorite horror movie?

Type 'a' for The Shining.
Type 'b' for Jaws.
Type 'c' for The Sixth Sense.
""")

movie = input("Answer: ")

if movie == "a":
	j = 1
	while j <= 10:
		print("ALL WORK AND NO PLAY MAKE JACK A DULL BOY")
		j += 1
elif movie == "b":
	print("Is your boat big enough?")
	boat = input("Type 'y' or 'n': ")
	if boat == "y":
		print("You're still probably going to need a bigger boat.")
	elif boat == "n":
		print("You're going to need a bigger boat.")
	else:
		print("I'm not sure what you meant, but maybe get a bigger boat, just in case.")
elif movie == "c":
	print("Do you see dead people?")
	ghost = input("Type 'y' or 'n': ")
	if ghost == "y":
		print("Don't worry. They're just looking for your help with something.")
	elif ghost == "n":
		print("Don't worry. You're normal. Or possibly, you're already dead and don't know it.")
	else:
		print("I'm not sure what you meant, but in case you do see dead people, lend a helping hand.")
else:
	print("Not one of those three? I guess there's no accounting for taste.")



sys.exit(0)