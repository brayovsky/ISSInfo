# ISSInfo
ISSInfo contains is a program that uses NASA's Open Notify API to report the number of people in space and the location of the International Space Station 

# How to use
ISSInfo is a command line application. The following are the list of commands available in the program

1. iss -p
Get the current position of the International Space Station. The following information is returned.  
	i. Current timestamp.  
	ii. Position of the ISS(Longitude and Lattitude in degrees).  

2. iss -n
Get the number of people in space. The following information is returned  
	i. Number of people.  
	ii. The information about each person.  
		a. The name of the craft they are in.  
		b. The name of the person.  

3. iss -x
Exit the program

#About Open Notify API
Information about the Open Notify API can be found at http://open-notify.org/

#Python version
Created in python version 2.6.6