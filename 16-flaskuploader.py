# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import json
import smtplib
from email.message import EmailMessage

from flask import Flask,render_template,request,redirect,url_for,send_file
from werkzeug import secure_filename
import pandas as pd
import numpy as np
import matplotlib as plt
import graphin

app = Flask(__name__)

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods=["POST"])
def uploader():
    if request.method=="POST":
        mysteryfile = request.files["file"]
        mysteryfile.save(secure_filename(mysteryfile.filename))
        if "cap" in mysteryfile.filename:
            return redirect(url_for("sip", filetoparse=mysteryfile.filename))
        elif "xlsx" in mysteryfile.filename:
            return redirect(url_for("excel", filetoparse=mysteryfile.filename))
        else:
            return " That format is not yet supported. please check back soon"

@app.route("/excel/<filetoparse>")
def excel(filetoparse):
    return send_file(graphin.pygraph(filetoparse),mimetype="image/png") 
    


@app.route("/sip/<filetoparse>")
def sip(filetoparse):
    sipjson=[]
    with open(filetoparse) as capture:
        for line in capture:
            matchobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)",line)
            if matchobj:
                tinylist=[]
                tinylist.append(matchobj.group())
                tinylist.append(matchobj.group(1))
                tinylist.append(matchobj.group(2))
                tinylist.append(matchobj.group(3))
                sipjson.append(tinylist)
        return json.dumps(sipjson) 

@app.route("/emailsender")
def emailsender():
    msg=EmailMessage()
    msg['Subject'] = "this is my subject line"
    msg['Srom'] = "Pythonstudent01@mail.com"
    msg['To'] = "rzfreeserspam@gmail.com"
    msg.preamble = " Thank you for troubleshooting almost everycode I wrote :)  from Prabodh Maisuri" 

    with open("/home/student/emailpassword.txt") as emailpass:
        myemailpass=emailpass.read().rstrip("\n") 
    mail = smtplib.SMTP("smtp.mail.com",587)
    mail.starttls()
    mail.login("pythonstudent01@mail.com",myemailpass)
    mail.sendmail("pythonstudent01@mail.com","rzfeeserspam@gmail.com",msg.as_string())
    mail.quit()
    return "Spammity spamcakes Sent"



if __name__ == "__main__":
    app.run(port = 5006)
