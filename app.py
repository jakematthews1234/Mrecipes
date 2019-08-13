import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from forms import EditRecipeForm, AddRecipeForm
import re


# connect to mongodb
app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.recipebook

# CSRF and Secret Key
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


# default route
@app.route('/')
@app.route('/home')
def index():
    """ default home route """
    recipes = db.recipes.find().limit(20)
    return render_template('index.html', recipes=recipes, title="HOME")


@app.route('/add_recipe', methods=['POST', 'GET'])
def add_recipe():
    """ adding a recipe to the database through the use of POST method """
    form = AddRecipeForm(request.form)
    if form.validate_on_submit():
        recipes = db.recipes
        recipes.insert_one({
            "recipe_name": request.form['recipe_name'],
            "author": request.form['author'],
            "cook_time": request.form['cook_time'],
            "level": request.form['level'],
            "ingredients": request.form['ingredients'],
            "method": request.form['method'],
            "servings": request.form['servings'],
        })
        return redirect(url_for("index", title="Recipe added"))
    return render_template("add_recipe.html", title="Add a recipe", form=form)


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """ creating an option for users to edit an existing recipe by finding the existing recipe
    in the database"""
    recipe_db = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "GET":
        form = EditRecipeForm(data=recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = db.recipes
        """ retrieving the information from the database and displaying it in the form so it can be 
        edited by the user easily"""
        recipes_db.update_one({
            '_id': ObjectId(recipe_id)
        }, {
            '$set': {
                "recipe_name": request.form['recipe_name'],
                "author": request.form['author'],
                "cook_time": request.form['cook_time'],
                "level": request.form['level'],
                "ingredients": request.form['ingredients'],
                "method": request.form['method'],
                "servings": request.form['servings'],

            }
        })
        return redirect(url_for("index"))
    return render_template("edit_recipe.html", recipe=recipe_db, form=form)

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """ allowing users to delete recipes easily with a click of a button"""
    db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))

@app.route('/search')
def search():
    """ for search bar """
    user_search = request.args["query"]
    """ line below was created by my tutor, and not myself """
    query = {'$regex': re.compile('.{}.'.format(user_search)), '$options': 'i'}
    results = db.recipes.find({
        '$or':
            [
                {"recipe_name": query},
                {"ingredients": query},
            ]
    })
    return render_template('search.html', query=user_search, results=results)

# flask set up

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = False
    app.config['DEBUG'] = False
    app.run(host='127.0.0.1', debug=True)
