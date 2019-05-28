import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

#connect to mongodb
app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.recipebook


@app.route('/')
#returning the index.html template
def index():
    recipes = [recipe for recipe in db.recipes.find({})]
    return render_template('index.html', recipes=recipes)

#setting up flask
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)