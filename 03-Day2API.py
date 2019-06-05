#!/usr/bin/python3
"""Learning about API"""

import json
import urllib.request 

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():

    # make request 
    resp = urllib.request.urlopen(MAJORTOM)
    

    # make Pythion strip json data from the 200 response

    jstring = resp.read()

    
    pyj = json.loads(jstring.decode('utf-8')) 

    # parse out json response 
    
    astrocosmo = pyj.get("people")


    for spaceperson in astrocosmo:
        print(spaceperson["name"])


    #display selected data on a screen - names of people in space


if __name__ == "__main__":
    main()



