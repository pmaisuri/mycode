#!/usr/bin/python3

from flask import Flask , redirect, url_for, request

app = Flask(__name__)


@app.route("/success/<name>")
def success(name):
    return "welcome{}".format(name)

@app.route("/login",methods = ["post","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
    else:
        user=request.args.get("nm")
    return redirect(url_for("success",name=user))

if __name__ == "__main__":
    app.run(port=5006)
