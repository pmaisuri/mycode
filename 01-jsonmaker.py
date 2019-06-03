#!/usr/bin/python3
"""now you have color"""

#with python jason batteries are included but you need to plug them in

import json

def main():

#Create a list of games dictionaires

    videogames=[{"game1":"red dead redumption","game2":"witcher","game3":"starcraft","game4":"faster than light"},{"game1":"paperboy","game2":"donkey kong"}]

#print value of video game 

    print(videogames)

#create a local files
    with open("videogames.json","w") as vidfile: #"w"=write "r"=read "a"=append
        json.dump(videogames,vidfile)


if __name__=="__main__":
    main()

