#!/usr/bin/python3
"""regex from the cap file"""

import re 

def main():
    with open("testcap.txt","r") as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)", line)
            #print(line)
            #regmatch = re.search(r"^Contact:", line)
            if regmatch:
                print(regmatch)
                print(regmatch.group())
                print(regmatch.group(1))
                print(regmatch.group(2))
                print(regmatch.group(3))

if __name__ == "__main__":
    main()
