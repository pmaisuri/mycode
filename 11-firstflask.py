#!/usr/bin/python3
"""creat flask"""

from flask import Flask

app = Flask(__name__)# always do this for flask

@app.route("/") # when you go to ROOT of your server do the following

def endoftheday():# function to triggerat root

    return"class is nearing the end for Wednesday" # RETURN this if you goto ROOT


@app.route("/hello/<name>",defaults={'position':'Administrative Assistant'})
@app.route("/hello/<name>/<position>")

def hellostudent(name,position):

    return "Hello {0} {1},Please to meet you {1}" .format(name,position)

    #return"welcome to class.." + name


if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
