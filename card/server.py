# -*- coding:utf8 -*-
# AUTHOR = 'kiddguo'
from flask import Flask
from settings import MONGO_URI, MONGO_DATABASE
from flask import render_template
import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    return "This is the index page"

@app.route('/mycard/')
def my_card():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    values = db["CardItem"].find()
    client.close()
    return render_template("mycard.html", values = values)

if __name__ == "__main__":
    app.run()