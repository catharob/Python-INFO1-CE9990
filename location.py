"""
location.py

A python module for getting latitudes and longitudes.

"""
import sys
import urllib.request
import json

class Location(object):

	def __init__(self, latitude, longitude):
		if not isinstance(latitude, int or float):
			raise TypeError("latitude must be int or float, not " + str(type(latitude)))
		if latitude > 90 or latitude < -90:
			raise ValueError("latitude must be in range -90 to 90")
		if not isinstance(longitude, int or float):
			raise TypeError("longitude must be int or float, not " + str(type(longitude)))
		if longitude > 180 or longitude < -180:
			raise ValueError("longitude must be in range -180 to 180")
		self.latitude = latitude
		self.longitude = longitude

	def getLatitude(self):
		"Return latitude."
		return self.latitude

	def getLongitude(self):
		"Return longitude."
		return self.longitude

	def __str__(self):
		if latitude >= 0 and longitude >= 0:
			return "{}\u00B0N {}\u00B0E".format(self.latitude, self.longitude)
		elif latitude < 0 and longitude >= 0:
			return "{}\u00B0S {}\u00B0E".format(self.latitude, self.longitude)
		elif latitude < 0 and longitude < 0:
			return "{}\u00B0S {}\u00B0W".format(self.latitude, self.longitude)
		else:
			return "{}\u00B0N {}\u00B0W".format(self.latitude, self.longitude)

	def setLatitude(self):
		"Change latitude"
		self.__init__

	def setLongitude(self):
		"Change longitude"
		self.__init__

	def getZipcode(self):
		"get zip code for a lat and long"
		url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(self.latitude) + "," + str(self.longitude)

		try:
			infile = urllib.request.urlopen(url)
		except urlib.error.URLError as error:
			print("urllib.error.ULRError", error)
			sys.exit(1)

		sequenceOfBytes = infile.read()
		infile.close()

		try:
			s = sequenceOfBytes.decode("utf-8")
		except UnicodeError as unicodeError:
			print(unicodeError)
			sys.exit(1)

		try:
			dictionary = json.loads(s)
		except json.JSONDecodeError as jSONDecodeError:
			print(jSONDecodeError)
			sys.exit(1)

		try:
			results = dictionary["results"]
		except ValueError:
			return 0

		firstResult = results[0]
		try:
			address_components = firstResult["address_components"]
		except ValueError:
			return 0

		for component in address_components:
			if "postal_code" in component["types"]:
				try:
					return int(component["long_name"])
				except ValueError:
					print("zip code not an integer")
					sys.exit(1)

if __name__ == "__main__":
	lat = 40
	lon = -74
	p = Location(lat, lon)
	print("the latitude and longitude are ", p, ".", sep = "")
	sys.exit(0)






