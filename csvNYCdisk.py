"""
csvNYCdisk.py

Put in your zip code, and I'll tell you how many noise complaints there were from 2015 to now.

"""

import sys
import csv   

filename = "/Users/Catherine/Documents/Python Practice Programs/NYU Class/csvNYCdisk/311_Service_Requests_from_2015.csv"


try:
    csvfile = open(filename, encoding = "utf-8", newline = "")
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

zipCode = input("Please enter a New York City zip code: ")
print("One moment please...")
n = 0

lines = csv.reader(csvfile)

for line in lines:              
    if line[8] == zipCode and "Noise" in line[5]:  #finds noise complaints in zip code user chooses
        n +=1  #counts instances of the zip entered

csvfile.close()

print("There have been", n, "noise complaints in", zipCode, "from the start of 2015 to July 19, 2017.")


sys.exit(0)
