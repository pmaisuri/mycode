#!/usr/bin/python3

import json,time,sqlite3,requests

def walmartlookup(walmarturl,mykey,upckey):
    try:
        walmarturlobj=requests.get(walmarturl+mykey+upkey)
        return walmarturlobj.json()
    except:
        return False

def trackmeplease(tracktime,trackprice):
    conn = sqlite3.connect("price.db")
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME VARCHAR2 PRIMARY KEYNOT NULL,
        PRICE REALNOT NULL;''')
    except:
        pass
    conn.execute("INSURT INTO PRICE(TIME ,PRICE) VALUES(?,?)",(tracktime,trackprice))
    conn.commit()
    cursor = conn.execute("SELECT time,price from PRICE")
    for row in cursor:
        print("TIME=",row[0])
        print("PRICE=",row[1])
    print("DATABASE OPERATION COMPLTE!")
    conn.close()

def main():

    wurl="http://api.walmartlabs.com/v1/items?"
    
    wkey="agfaekhfn7bcq6bfkxwke2wg"
    wkey="apiKey="+wkey
    
    wupc="035000521019"
    wupc="&upc="+wupc

    print("Walmart query urlis:",wurl,wkey,wupc,sep="")
    
    decodedwalmart = walmartlookup(wurl,wkey,wupc)

    if decodedwalmart:
        print("\n walmart price on",time.ctime(),":$",str(decodedwalmart["items"][0]["salePrice"]))
        
        tracmeplease(time.ctime(),decodedwalmart["items"][0]['salePrice'])

    else:
        print("Something went wrong")
        
if __name__ == "__main__":
    main()

