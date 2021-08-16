#importing flask, render_template to create pages, request to grab data from form, session to store session data, and flash to display errors
#and redirect to move to new route after taking in form data
from flask import Flask, render_template, redirect, request, session, flash # Import Flask to allow us to create our app
from flask_app.models.recipe import Recipe #always import the classes from the model
from flask_app import app, bcrypt

from flask_app.models.user import User


@app.route("/newrecipe/validate")
def new_recipe():
    if not "unique_userid" in session:
        return redirect("/")

    dict = {"id": session["unique_userid"]}

    #pass the entire table, and pass in the current logged in user
    return render_template("create_recipe.html", logged_user = User.get_one(dict))


@app.route("/newrecipe/create", methods = ['POST'])
def create_recipe():
    if not recipe.validate_recipe(request.form):
        return redirect("/newrecipe/validate")
    
    form_data = { **request.form, "user_id": session['unique_userid']} # This is how to insert user id into creating something 
    
    recipe.create(form_data) # Using the variable we just created form_data
    

    return redirect("/users/page")


@app.route("/listrecipes/<int:id>/view")
def view_recipe(id):

    dict = {"id": id}

    return render_template("recipe_list.html", 
    user = User.get_one_join(dict), 
    logged_user = User.get_one( {"id": session['unique_userid']}), 
    user_name = User.get_one(dict))



@app.route("/listrecipes/<int:recipe_id>/edit")
def edit_recipe(recipe_id):

    dict2 = {"id": recipe_id}

    return render_template("edit_recipe.html", logged_user = User.get_one( {"id": session['unique_userid']}), recipe = recipe.get_one(dict2))
    # The variables in this line give the template access to specific info, passing in logged_in user and the users recipe

@app.route("/existing_recipe/<int:id>/edit", methods = ['POST'])
def edit_recipeform(id):
    if not recipe.validate_recipe(request.form):
        return redirect("/users/page")
    
    form_data = { **request.form, "id": id} # This is how to insert user id into creating something 
    
    recipe.update(form_data) # Using the variable we just created form_data
    

    return redirect("/users/page")


@app.route("/delete/<int:id>/recipe")
def delete_recipe(id):

    dict = {"id": id}
    recipe.delete(dict)

    return redirect("/users/page")
    