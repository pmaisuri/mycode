#!/usr/bin/python3
"""Learning about API"""

import requests


MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    try:


    # make request 
        resp = requests.get(MAJORTOM)
    
    #convert string data to json

        pyj = resp.json()

    # parse out json and we strip off the response 

        astrocosmo = pyj.get("people")


        for spaceperson in astrocosmo:
            print(spaceperson["name"])
    
    except:
        print("API is not available at the moment")
        exit()

    #display selected data on a screen - names of people in space


if __name__ == "__main__":
    main()



