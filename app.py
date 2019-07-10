import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint
import json

# connect to mongodb
app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.recipebook


# default route
@app.route('/')
@app.route('/home')
def index():
    """ default home route """
    recipes = [recipe for recipe in db.recipes.find({})]
    return render_template('index.html', recipes=recipes, title="HOME")


@app.route('/add_recipe', methods=['POST', 'GET'])
def add_recipe():
    """ adding a recipe to the database through the use of POST method """
    recipes = db.recipes

    if request.method == "POST":
        recipe = request.form.to_dict()
        recipes.insert_one(recipe)
        return redirect(url_for('add_recipe'))
    return render_template('addrecipe.html')


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """ creating an option for users to edit an existing recipe by finding the existing recipe
    in the database"""
    the_recipe = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)


@app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
def update_recipe(recipe_id):
    recipe = db.recipe
    recipe.replace_one({'_id': ObjectId(recipe_id)},
                 {
                     'recipe_name': request.form.get('recipe_name'),
                     'Author': request.form.get('Author'),
                     'cook_time': request.form.get('task_description'),
                     'Level': request.form.get('Level'),
                     'Ingredients': request.form.get('Ingredients'),
                     'Method': request.form.get('Method'),
                     'Servings': request.form.get('Servings')
                 })
    return redirect(url_for('index', recipe_id=recipe_id))


# setting up flask

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
