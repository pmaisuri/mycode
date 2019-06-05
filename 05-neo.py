#!usr/bin/python3
""" Creat Near Earth object """

import requests


# from pprint liberary use pprint function and define as pp for this code 

#from pprint import pprint as pp

MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key="


def keyharvester():
    with open("/home/student/nasa.key","r") as keyfile:
        mykey = keyfile.read()
        return mykey

def main():

    #harvest our key from /home/student/nasa.key
    nasakey = keyharvester()
    nasakey = nasakey.rstrip('\n')

    #appened our key to MYAPI
    #Call the  API (requests.get()) 
    # also in the json format .json()
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()
    

    # Parse  jason  - loop  across " near_earth_objects" to reveal asteroids
    
    for bigrock in asteroidz["near_earth_objects"]:
        if bigrock["is_potentially_hazardous_asteroid"]:
            print("Name -   " ,bigrock["name"])
            print("proximity -  ",bigrock["close_approach_data"])
            print("Size -     ",bigrock["estimated_diameter"], end="\n***********************\n") 
       # else:
        #    print("This asteroid is not dangerous")
            

    # only display those that may pose a danger to Human kind

if __name__ == "__main__":
    main()

