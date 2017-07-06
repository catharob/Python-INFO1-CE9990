"""
vowelMuncher.py

This is the program that 'does something interesting with for loops and if statements.'

It's a little vowel-eating monster.

"""

vowels = "aeiou"

word = input("Please type a word: ")

v = 0

def eatTheVowels(word, v):
	for w in word:
		if w in vowels:
			word = word.replace(w, "")
			v +=1

	print("Yum, vowels! Here's what's left: "+ word)
	if v < 10:
		newword = input("Still hungry! Type another word: ")
		eatTheVowels(newword, v)
	else:
		print("So full! Thanks for feeding me 10 vowels!")

eatTheVowels(word, v)




