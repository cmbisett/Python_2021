from flask import Flask, render_template, redirect, request, session, flash 
from flask_app.models.sighting import Sighting 
from flask_app import app, bcrypt
from flask_app.models.user import User


@app.route("/newsighting/validate")
def new_sighting():
    if not "unique_userid" in session:
        return redirect("/")

    dict = {"id": session["unique_userid"]}

    #pass the entire table, and pass in the current logged in user
    return render_template("create_sighting.html", logged_user = User.get_one(dict))


@app.route("/newsighting/create", methods = ['POST'])
def create_sighting():
    if not Sighting.validate_sighting(request.form):
        return redirect("/newsighting/validate")
    
    form_data = { 
        **request.form, 
        "user_id": session['unique_userid']
        }  
    
    Sighting.create(form_data) # Using the variable we just created form_data
    

    return redirect("/dashboard")


@app.route("/listsightings/<int:id>/view")
def view_sightings(id):

    dict = {"id": id}

    return render_template("sighting_list.html", 
        user = User.get_one_join(dict), 
        logged_user = User.get_one( {"id": session['unique_userid']}), 
        user_name = User.get_one(dict), 
        all_sightings = Sighting.get_all(), 
        sighting = Sighting.get_one(dict)
    )



@app.route("/listsightings/<int:sighting_id>/edit")
def edit_sighting(sighting_id):

    dict2 = {"id": sighting_id}

    return render_template("edit_sighting.html", logged_user = User.get_one( {"id": session['unique_userid']}), sighting = Sighting.get_one(dict2))
    

@app.route("/existing_sighting/<int:id>/edit", methods = ['POST'])
def edit_petform(id):
    if not Sighting.validate_sighting(request.form):
        return redirect("/dashboard")
    
    form_data = { 
        **request.form, 
        "id": id
    }  
    
    Sighting.update(form_data) # Using the variable we just created form_data
    

    return redirect("/dashboard")


@app.route("/delete/<int:id>/sighting")
def delete_sighting(id):

    dict = {"id": id}
    Sighting.delete(dict)

    return redirect("/dashboard")
    