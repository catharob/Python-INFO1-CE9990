"""
csvNYCweb.py

I'd like this to read from 311 NYC data and find something to match a zip code.
But I'm getting an odd error: "DECRYPTION_FAILED_OR_BAD_RECORD_MAC]"
Posting this in case someone knows how to fix, and switching gears to read file from disk instead.

"""

import sys
import csv   #Comma-separated values.  Do not name this Python script csv.py.
import urllib.request

url = "https://data.cityofnewyork.us/api/views/erm2-nwe9/rows.csv?accessType=DOWNLOAD"

try:
    lines = urllib.request.urlopen(url)

except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)


noiseLines = []                   #Start with an empty list.

for line in lines:
    try:
        s = line.decode("utf-8")    #s is a string
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    r = csv.reader([s])         #[s] is a list containing one string
    fields = next(r)            #fields is a list of strings
    if fields[0] =="36723855": #zip code match and finding noise complaint
        print(fields[0])


# print(noiseLines)
lines.close()
sys.exit(0)