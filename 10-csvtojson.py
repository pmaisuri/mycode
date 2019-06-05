#!/usr/bin/python3
"""Reading CSV file"""

import csv
import json

def main():
    
    jsonf=open("supercar.json","w") 

    with open("supercar.csv",newline="") as csvf:
        reader=csv.DictReader(csvf)
        
        json.dump(list(reader),jsonf)


    jsonf.close()

if __name__=="__main__":
    main()
