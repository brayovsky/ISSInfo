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
        position_dict = self.__make_API_request(self.position_endpoint)
        return position_dict


    #get the number of people in space
    def get_people_in_space(self):
        people_dict = self.__make_API_request(self.people_in_space_endpoint)
        return people_dict

    #make the request using API
    def __make_API_request(self,endpoint):
        req = urllib2.Request(endpoint)
        response = urllib2.urlopen(req)
        obj = json.loads(response.read())
        return obj


#class to hold methods for displaying and taking input from the user
class DisplayUI(object):
    def __init__(self):
        print("Welcome to the ISS monitor")
        self.get_space = SpaceInfo("http://api.open-notify.org/iss-now.json","http://api.open-notify.org/astros.json")
        self.instruction_and_pomp_display()

    def instruction_and_pomp_display(self):
        os.system('clear')
        print("------------------------------------------------------------")
        print("|                  ISS Monitor                              |")
        print("------------------------------------------------------------")
        print(" To know number of people in space type 'iss -n'")
        print(" To know position of iss type 'iss -p'")
        print(" To exit type 'iss -x'")
        self.main_display()

    def main_display(self):
        choice = ''
        while choice != 'exit':
            choice = raw_input("What would you like to get? ")
            print(choice)
            if choice == 'iss -n':
                self.__process_dict_to_view(self.get_space.get_people_in_space())
            elif choice == 'iss -p':
                self.__process_dict_to_view(self.get_space.get_iss_position())
            elif choice == 'iss -x':
                choice = "exit"               
            else:
                print("\nI didn't understand that choice.\n")

    def __process_dict_to_view(self,dict_item):
        if type(dict_item)==type([]):
            for key,val in enumerate(dict_item):
                if key=='message':
                    continue
                if type(val)==type({}) or type(val)==type([]):
                    print("%s:"%key)
                    self.__process_dict_to_view(val)
                else:
                    print("%s : %s"%(key,val))
        elif type(dict_item)==type({}):
            for key,val in dict_item.iteritems():
                if key=='message':
                    continue
                if type(val)==type({}) or type(val)==type([]):
                    print("%s:"%key)
                    self.__process_dict_to_view(val)
                else:
                    print("%s : %s"%(key,val))



if __name__ == '__main__':
    display = DisplayUI()
