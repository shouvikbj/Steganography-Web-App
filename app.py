from flask import Flask, render_template, redirect, request, url_for, flash
import os
import json
import copy
import uuid

from LSBSteg import *

app = Flask(__name__, static_url_path="")
app.secret_key = "this is a secret key"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encrypt")
def encrypt():
    return render_template("encrypt.html")

@app.route("/encryptimage", methods=["POST"])
def encryptimage():
    target = APP_ROOT+'/static'
    filename = "myimage.jpg"
    image_file = request.files.get("image")
    text = request.form.get("text")
    destination = "/".join([target,filename])
    image_file.save(destination)
    steg = LSBSteg(cv2.imread(f"{APP_ROOT}/static/myimage.jpg"))
    img_encoded = steg.encode_text(text)
    cv2.imwrite(f"{APP_ROOT}/static/new_image.png", img_encoded)
    return redirect("/afterencryption")

@app.route("/afterencryption")
def afterencryption():
    return render_template("afterencryption.html")

@app.route("/decrypt")
def decrypt():
    return render_template("decrypt.html")

@app.route("/decryptimage", methods=["POST"])
def decryptimage():
    target = APP_ROOT+'/static'
    filename = "new_image.png"
    image_file = request.files.get("image")
    destination = "/".join([target,filename])
    image_file.save(destination)
    im = cv2.imread(f"{APP_ROOT}/static/new_image.png")
    steg = LSBSteg(im)
    text = steg.decode_text()
    # print("Text value:",steg.decode_text())
    return render_template("afterdecryption.html", text=text)

@app.route("/afterdecryption")
def afterdecryption():
    return render_template("afterdecryption.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
