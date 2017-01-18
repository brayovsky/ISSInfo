import urllib2
import json
import os

#class to hold the methods for accessing Open Notify API
class SpaceInfo(object):
	def __init__(self):
		pass

	#get the position of the ISS
	def get_iss_position(self):
		pass

	#get the number of people in space
	def get_people_in_space(self):
		pass

	#make the request using API
	def __make_API_request(self,endpoint):
		pass

#class to hold methods for displaying and taking input from the user
class DisplayUI(object):
	def __init__(self):
		pass

	def main_display(self):
		pass

if __name__ == '__main__':
    input("Hi. All good")
