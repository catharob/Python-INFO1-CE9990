"""

cometLyrics.py

Prints an abridged version of the lyrics to the Prologue of Natasha and Pierre and the Great Comet of 1812.

"""

prologueIntro = [
    "There's a war going on",
    "Out there somewhere",
    "And Andrey isn't here",
    "And this is all in your program",
    "You are at the opera",
    "Gonna have to study up a little bit if you wanna keep with the plot",
    "Cuz it's a complicated Russian novel",
    "Everyone's got nine different names",
    "So look it up in your program",
    "We'd appreciate it, thanks a lot"
]

characters = [
    "Andrey isn't here",
    "Natasha is young",
    "Sonya is good",
    "Marya is old-school",
    "Anatole is hot",
    "Helene is a slut",
    "Dolokhov is fierce",
    "Mary is plain",
    "Bolonsky is crazy",
    "Balaga is fun",
]

pierre = [
    "What about Pierre?",
    "Dear bewildered and awkward Pierre? What about Pierre?",
    "Rich, unhappily married Pierre? What about Pierre?"
]

def printIntroInterludePierre(lyrics):
	for lyric in lyrics:
		print(lyric)

def printCharacters(lyrics):
	for n in range(len(lyrics)):
		for i in range(n, 0, -1):
			print(lyrics[i])
		print("And Andrey isn't here.")
		print()


printIntroInterludePierre(prologueIntro)

printCharacters(characters)

printIntroInterludePierre(pierre)