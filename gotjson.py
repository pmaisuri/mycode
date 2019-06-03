#!/usr/bin/python3
"""Author prabodh json file excercise"""

#pull in json lib so we can parse out json
import json

def main():
    #open the jonsnow.jason file in the read mode
    with open("jonsnow.json","r") as gotdata:
        jonsnow = gotdata.read()
        GOTpy = json.loads(jonsnow) #creat a STRING of all the json
        print(GOTpy) # get the GOT data
        print(GOTpy["url"])# display URL
        print(GOTpy["titles"][0]) # display title only
        print(GOTpy["aliases"])#display just the alias

    with open("aliases.txt","w") as jsaliases:
        for gotalias in GOTpy["aliases"]:
            print(gotalias,file=jsaliases)

    print(GOTpy["aliases"])    

    
if __name__ == "__main__":
    main()

