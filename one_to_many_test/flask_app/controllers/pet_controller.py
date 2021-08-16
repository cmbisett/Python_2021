#importing flask, render_template to create pages, request to grab data from form, session to store session data, and flash to display errors
#and redirect to move to new route after taking in form data
from flask import Flask, render_template, redirect, request, session, flash # Import Flask to allow us to create our app
from flask_app.models.pet import Pet #always import the classes from the model
from flask_app.models import user
from flask_app import app, bcrypt


@app.route('/newpet/validate')
def new_pet():
    if "unique_userid" not in session:
        return redirect("/users")

    dict = {"id": session["unique_userid"]}

    #pass the entire table, and pass in the current logged in user
    return render_template("create_pet.html", logged_user = user.User.get_one(dict))


@app.route("/newpet/create", methods = ["POST"])
def create_pet():
    if not Pet.validate_pet(request.form):
        return redirect('/newpet/validate')


    form_data = {     #this is how to insert user id session data into creating something
        **request.form,
        "user_id": session['unique_userid']
    }
    Pet.create(form_data)

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'unique_userid' not in session:
        return redirect('/')

    dict = {"id": session["unique_userid"]}

    return render_template("pet_list.html", all_pets = Pet.get_all(), logged_user = user.User.get_one(dict))