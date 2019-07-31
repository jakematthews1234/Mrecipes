from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EditRecipeForm(FlaskForm):
    """ form for edit recipe """
    recipe_name = StringField("Recipe Name", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    cook_time = StringField("Cook Time", validators=[DataRequired()])
    level = StringField("Level of Difficulty", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients(one per line)", validators=[DataRequired()])
    method = TextAreaField("Method(one per line)", validators=[DataRequired()])
    servings = StringField("No. of Servings", validators=[DataRequired()])
    submit = SubmitField("Update Recipe")


class AddRecipeForm(FlaskForm):
    """ form for edit recipe """
    recipe_name = StringField("Recipe Name", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    cook_time = StringField("Cook Time", validators=[DataRequired()])
    level = StringField("Level of Difficulty", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients(one per line)", validators=[DataRequired()])
    method = TextAreaField("Method(one per line)", validators=[DataRequired()])
    servings = StringField("No. of Servings", validators=[DataRequired()])
    submit = SubmitField("Update Recipe")