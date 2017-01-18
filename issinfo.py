import urllib2
import json
import os

#class to hold the methods for accessing Open Notify API
class SpaceInfo(object):
	def __init__(self,position_endpoint,people_in_space_endpoint):
		self.position_endpoint = position_endpoint
		self.people_in_space_endpoint = people_in_space_endpoint

	#get the position of the ISS
	def get_iss_position(self):
		print("ge")
		position_dict = self.__make_API_request(self.position_endpoint)
		print position_dict

	#get the number of people in space
	def get_people_in_space(self):
		people_dict = self.__make_API_request(self.people_in_space_endpoint)
		print people_dict

	#make the request using API
	def __make_API_request(self,endpoint):
		req = urllib2.Request(endpoint)
		response = urllib2.urlopen(req)
		obj = json.loads(response.read())
		return obj

#class to hold methods for displaying and taking input from the user
class DisplayUI(object):
	def __init__(self):
		pass

	def main_display(self):
		pass

if __name__ == '__main__':
    get_space = SpaceInfo("http://api.open-notify.org/iss-now.json","http://api.open-notify.org/astros.json")
    get_space.get_iss_position()
    get_space.get_people_in_space()
    input("Hi. All good")
