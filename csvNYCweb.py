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

for i, line in enumerate(lines):
    try:
        s = line.decode("utf-8")    #s is a string
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    r = csv.reader([s])         #[s] is a list containing one string
    fields = next(r)
          #fields is a list of strings
    print(fields[0])
    if i >= 50:
        break


# for n, line in enumerate(lines): 
#     for i in range(n, 0, -1): #here, trying to make it read from the topmost or latest entry in the data...
#                                 #rather than the first or bottom entry
#         try:
#             s = line.decode("utf-8")    #s is a string
#         except UnicodeError as unicodeError:
#             print("unicodeError")
#             sys.exit(1)

#         r = csv.reader([s])         #[s] is a list containing one string
#         fields = next(r) 


#         if "08/04/2017" in fields[1]:  #trying to find just records entered on one day
#             print(fields)




# print(noiseLines)
lines.close()
sys.exit(0)