"""
vowelMuncher.py

This is the program that 'does something interesting with for loops and if statements.'

It's a little vowel-eating monster.

"""

import sys

vowels = "aeiou"


n = 10
v = 0

def eatTheVowels(word, v):
	while True:
		for w in word:
			if w in vowels:
				word = word.replace(w, "")
				v +=1

		print("Yum, vowels! Here's what's left: "+ word)
		if v >= n:
			print("So full! Thanks for feeding me", n, "vowels!")
			break
		word = input("Still hungry! Type another word: ")

word = input("Please type a word: ")
eatTheVowels(word, v)
sys.exit(0)




