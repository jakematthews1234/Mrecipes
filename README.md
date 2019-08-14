# Mrecipes 

## __PROJECT OVERVIEW__
This is my third of four projects within the CodeInstitute course. In this project I focused on using Python
along with other coding languages such as HTML and CSS to create a web page which is capable of storing 
recipes within a Database. I then ensured that the Recipe entries are able to be 
1. Created
1. Readable
1. Updated
1. Deleted
 
by anyone (users) who have access to the website. I also wanted the users to have the option to use the 
website as a 'recipe-book' style website, allowing for them to search for a specific recipe or just 
generally browse through the recipes to find one in which they wish to use. 

## __UX DESIGN__ 
* This site was created with the intention of allowing users to search for and find recipes for different
dishes throughout the world. 'Mrecipes' is typically aimed at the people who wish to learn how to cook
i.e. non experienced cooks. It is also aimed at more experienced 'cooks' who wish to share the recipes they
 have created with the world. Mrecipes allows users to use CRUD features in order to showcase recipes, 
or find recipes. Having CRUD features allows for the website to be in control of the users. My project
best allows users to find recipes as the entire site is dedicated to just that; Recipes!

## __USER STORIES__

* Joseph is relatively new to cooking and wishes to learn some basic recipes in order to begin having a 
more balanced diet. He wishes to find a website that can be easily navigated, to find simple and easy to 
read recipes for him to follow, step by step. 

My website would make it easy for Joseph to learn how to cook, as each recipe is easily displayed and 
accessed through the home page in order to make it easy for people to find a recipe they may enjoy. 
each recipe has a breakdown of ingredients required, and the method in which to follow in order to 
create the recipe.

* Dan is an experienced chef. He wishes for a place where he can put his recipes so that other people, 
like Joseph, have a place where they can go, to follow his recipes.

My website would make it easy for Dan to share his recipes with the world, through the use of the 'Add recipe'
function. This allows Dan to go into as much detail as he wishes about his recipes, so that others can read
and enjoy them.

* Georgia wishes to show her children how to cook, but lacks the knowledge or the experience requried to do so.
she wants a website she can show to her children, in which they can explore the different recipes and choose
ones that they would like to eat. 

My website would make it easy for Georgia's children to navigate as it is designed to be as simple as possible
so that people of all ages and abilities can use it effectively. I have ensured that the information architecture
is as strong as it can be, to solidify this. 

## __MOCKUPS__

My mockups are located as images in ../static/images

## __FEATURES__

* One of my features is the ability to 'Create' recipes. With this feature in place it allows all users to share
recipes with one another.

* Another feature I have in place is the ability to 'Read' all recipes within the Database. This allows all users
to read recipes that have been added by other people, giving them the chance to learn how to make that recipe.

* Another feature I have implemented is the ability to 'Update' any recipe stored within the Database. This allows
users to correct any mistakes that others may have made, or add improvements to the recipes.   

* Another feature I have in place is the ability to 'Delete' recipes from the database. With this feature in place
it allows users to delete old or outdated recipes, or even delete recipes in which they believe to be wrong. 

* I created a very basic navigation bar, with the purpose of allowing users to navigate the pages easier. With a home
button in place, and a "Add recipe" button, it allows for users to quickly get to pages, with ease.

* I created a basic search bar, with the purpose of allowing users to find specific recipes easily, or if they 
aren't sure what recipe they wish to look at, they can simply search an ingredient, so that options can become
available. 

## __FUTURE FEATURES__
 
* If this I was to continue with this project, the next thing I would implement would be the ability to sign in.
This would be a requirement to use CRUD features, so that it would lower the chances of people deleting valid recipes
from the database, or editing them stupidly.
* Another feature I would look at improving would be the search bar. At the moment it can only search for names, or 
ingredients, and is purely there at the moment just to showcase that the feature is there.

## __TECHNOLOGIES USED__

* HTML was used in order to create the web page.

* CSS was used in order to create the styling for certain parts of the webpage.

* Python was used to create all the functions for my web page. e.g. CRUD features.

* Javascript was used in order to use materialize
https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js

* Jquery was used in order to use materialize
https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js

* MongoDB was used in order to create and store my information in a database. 
https://www.mongodb.com/

* Materialize was used in order to aid me with certain styling and responsiveness.
https://materializecss.com/

* flask was used in order to use functions such as : render_template, redirect, request, url_for
https://flask.palletsprojects.com/en/1.1.x/

* re was used in order to make the search bar work properly.
https://regexr.com/

* bson was used in order for my edit recipe and delete recipe functions work properly using the objectID.
http://bsonspec.org/

* OS was used in order to successfully create a connection to my MongoDB.
https://docs.python.org/3/library/os.html


## __TESTING__
Throughout the project I have manually tested extensively in order to try find bugs that may cause problems
for my website, and have fixed them accordingly.

Each time I introduced a new feature, I tested it thoroughly, with the intention of trying to break the website, 
so that when my website is live, Users are unable to break it themselves. 
 
1. Add recipe form:
    1. Go to "Add recipe" page.
    1. Try to submit a recipe when the fields are empty.
    1. required field message is shown.
    1. no recipe is added.

I aimed to make my web pages as responsive as possible. This time round I didnt opt to use the "mobile first"
approach as the focus for this project was on the functions within the webpage, rather than the webpage itself.
If this project was to have been real, the Mobile first approach would have been used in order to maximise 
responsiveness for users. 
    
2. Open Chrome dev tools:
    1. Change the screen size.
    1. All elements on the page move according to screen size.
    1. no overlap is present.
    
### __INTERESTING BUGS__    


* One interesting bug that I encountered was my connection string kept breaking. I had to spend roughly 50 hours
speaking with different tutors, MongoDB support staff, C9 support staff, Codeinstitute staff, in order to try
get this problem fixed. In the end it had something to do with Cloud9 and so advice was given to me to change
from Cloud9 to Pycharm to code. Once this move was made, the connection remained intact and no further errors 
were found. I believe the problem was something to do with my cloud9 not having correct permissions, perhaps
due to the migration over to the new software. 

* One interesting bug that I found was that with using materialize's grid system, some things overlap.
The grid system doesnt seem to be as well structured as Bootstraps grid system, and is a lot more 
difficult to get right. Even when looking at the documentation of Materialize, the Nav-bar examples they show
also overlap. After speaking with my Tutor, we agreed that for future projects, Bootstrap should be used rather
than Materialize, for ease of use.

* Another interesting bug found was with my search bar. For some reason beyond my current knowledge, only certain
ingredients/words show up when searched for. For example, when Searching the word 'Chicken'; "Chicken and 
chorizo jambalaya" successfully displays as a search result. However, when searching the word 'Jambalaya'
the above recipe fails to show up. If this was to have been a real project, I would have spent additional
time debugging in an attempt to fix this issue, but as it was a course project, I decided that it would
take too much time, as the general function works successfully.              




