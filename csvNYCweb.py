"""
csvNYCweb.py

Takes an NYC zip code from user, takes a random slice of NYC 311 data, and filters for \
noise complaints in that zip code. 

"""
import datetime
import sys
import csv   
import urllib.request

url = "https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD"

try:
    lines = urllib.request.urlopen(url)

except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

while True:
    def score(fields):
        return datetime.datetime.strptime(fields[1], "%m/%d/%Y %I:%M:%S %p")

    zipCode = input("Please enter a 5 boros zip code: ")
    print("Here are noise complaints made in this zip code from a random sample of ten thousand 311 complaints.")

    noiseLines = []                   #Start with an empty list.

    for i, line in enumerate(lines):
        try:
            s = line.decode("utf-8")    #s is a string
        except UnicodeError as unicodeError:
            print(unicodeError)
            sys.exit(1)

        r = csv.reader([s])         #[s] is a list containing one string
        fields = next(r)            #fields is a list of strings

        if fields[8] == zipCode and "Noise" in fields[6]:
            noiseLines.append(fields)

        if i>=10000:
            break


    noiseLines.sort(key = score, reverse = True)

    if len(noiseLines) > 0:
        for line in noiseLines:
            print(line[1], line[8], line[5])
    else:
        print("Sorry, we couldn't find any noise complaints in that zip code.")

    while True:
        answer = input("Want me to try another sample? (y/n): ")
        if answer in ('y', 'n'):
            break
        else:
            print("Oops, I didn't catch that. Try 'y' or 'n'.")
    if answer == 'y':
        continue
    else:
        print("Okay bye.")
        break

lines.close()
sys.exit(0)