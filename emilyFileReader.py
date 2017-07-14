"""
emilyFileReader.py
Reads a poem and prints it out.
Then fixes all the improper capitalizations, with apologies to Emily Dickinson.
"""

import sys

def fixGrammar(line): #function to rewrite the poem getting rid of all capital letters except for proper "I"
	lineFixed = []
	lineSplit = line.split(" ")
	firstWord = lineSplit[0]
	lineFixed.append(firstWord)
	restOfLineSplit = lineSplit[1:]
	for word in restOfLineSplit:
		if word == "I":
			lineFixed.append(word)
		else:
			newWord = word.lower()
			lineFixed.append(newWord)
	lineFixed = " ".join(lineFixed)
	print(lineFixed, end="")


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

print()
print()

lines.seek(0)

print("***Great poem. But now let's fix the grammar.***")
print()


for line in lines:
	fixGrammar(line)


lines.close()
sys.exit(0)