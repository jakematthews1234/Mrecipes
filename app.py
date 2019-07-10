import os
from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from forms import EditRecipeForm
from config import Config

# connect to mongodb
app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.recipebook

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# default route
@app.route('/')
@app.route('/home')
def index():
    """ default home route """
    # recipes = [recipe for recipe in db.recipes.find({})]
    recipes = db.recipes.find()
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


@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """ creating an option for users to edit an existing recipe by finding the existing recipe
    in the database"""
    recipe_db = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if request.method == "GET":
        form = EditRecipeForm(data= recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = db.recipes
        recipes_db.update_one({
            '_id': ObjectId(recipe_id)
        }, {
            '$set': {
                "recipe_name": request.form['recipe_name'],
                "author": request.form['author'],
                "cook_time": request.form['cook_time'],
                "Level": request.form['level'],
                "Ingredients": request.form['ingredients'],
                "Method": request.form['method'],
                "Servings": request.form['servings'],

            }
        } )
        return redirect(url_for("index"))
    return render_template("edit_recipe.html", recipe=recipe_db, form=form)














    # the_recipe = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # return render_template('editrecipe.html', recipe=the_recipe)


# @app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
# def update_recipe(recipe_id):
#     recipe = db.recipe
#     form = request.form.to_dict()
#     if form:
#         print("update form valid")
#         recipe.update_one({'_id': ObjectId(recipe_id)},
#                      {
#                          '$set': {
#                              'recipe_name': request.form['recipe_name'],
#                              'author': request.form['author'],
#                              'cook_time': request.form['cook_time'],
#                              'Level': request.form['Level'],
#                              'Ingredients': request.form['Ingredients'],
#                              'Method': request.form['Method'],
#                              'Servings': request.form['Servings']
#                          }
#                      })
#         print(recipe)
#         return redirect(url_for('index', recipe_id=recipe_id))
#

# setting up flask

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = False
    app.config['DEBUG'] = False
    app.run(host='127.0.0.1', debug=True)
