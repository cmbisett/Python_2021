from flask import Flask, render_template, redirect, request, session, flash 
from flask_app.models.user import User 
from flask_app import app, bcrypt
from flask_app.models.sighting import Sighting

#index page, will start and display login and registration forms 
@app.route("/")
def index():
    # if there is a user in session, start on the user page
    if "unique_userid" in session:
        return redirect("/dashboard")

    return render_template("index.html")


#taking the form data from the registration portion of the index page
@app.route("/register/validate", methods=["POST"])
def valid_register():
    #validate all the input and redirect back to index with error messages displaying
    if not User.validate_registration(request.form):
        return redirect("/")


    #get the hash for the password 
    new_hash = bcrypt.generate_password_hash(request.form['password'])
    #store all the data from the new request.form 
    new_dict = {
        **request.form,
        "password": new_hash
    }
    
    #create the new user, and store the id into new_user variable
    new_user = User.create(new_dict) #will return new id of user from database

    session["unique_userid"] = new_user #pass the id into session 

    return redirect("/dashboard")


#This will validate and pass the form information for login
@app.route("/login/validate", methods=["POST"])
def valid_login():
    #validate all the input and redirect back to index with error messages displaying
    if not User.validate_login(request.form):
        flash("Cannot enter without logging in")
        return redirect("/")

    user = User.get_by_email({"email": request.form['email']}) #get the unique email, and store the id into session

    session["unique_userid"] = user.id

    return redirect("/dashboard")


#this route displays the users page after login
@app.route('/dashboard')
def user_page():
    if "unique_userid" not in session:
        return redirect("/")
    
    dict = {"id": session["unique_userid"]}

    return render_template(
        "sightings.html", 
        all_sightings = Sighting.get_all(), 
        user = User.get_one(dict)
    ) 
    # This displays all sightings



@app.route("/user/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/user/edit/<int:id>")
def update_user(id):
    if id != session['unique_userid']:
        return redirect("/dashboard")

    dict2 = {"id": session['unique_userid']}

    return render_template("edit_user.html", logged_user = User.get_one( {"id": session['unique_userid']}), user = User.get_one(dict2))    


@app.route("/user_edit/<int:id>", methods = ['POST'])
def edit_user_form(id):
    
    if not User.validate_registration(request.form):
        return redirect(f"/user/edit/{id}")
    form_data = { **request.form, "id": id} # This is how to insert user id into creating something 
    
    
    
    User.update(form_data) # Using the variable we just created form_data
    

    return redirect("/dashboard")