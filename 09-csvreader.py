#!user/bin/python3
"""Reading CSV file"""

import csv

def main():
    with open("supercar.csv",newline="") as csvf:
        reader=csv.DictReader(csvf)
        for row in reader:
            print(row["heroname"],"is",row["name"])

if __name__=="__main__":
    main()
