"""
drugDeath.py

Finds one record of an adverse drug event from the FDA in which someone died.

"""

import sys
import urllib.request as urlRequest
import json

url = 'https://api.fda.gov/drug/event.json?search=patient.reaction.reactionmeddrapt:"death"&limit=1'

infile = urlRequest.urlopen(url)

sequenceOfBytes = infile.read()         #Read the entire input file.
infile.close()

s = sequenceOfBytes.decode("utf-8")  #error checking omitted for brevity
dictionary = json.loads(s) 

print(json.dumps(dictionary, indent=4))

sys.exit(0)