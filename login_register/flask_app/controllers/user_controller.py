from flask import Flask, render_template, redirect, request, session, flash # Import Flask to allow us to create our app
from flask_app import app, bcrypt
from flask_app.models.user import User

@app.route("/")
def index():
    # if "uuid" in session:
    #     return redirect("/users")
    return render_template('index.html')


@app.route('/users')
def display_users():
    # if "uuid" not in session:
    #     flash("Must log in")
    #     return redirect('/')

    return render_template("success.html", all_users = User.get_all(), user = User.get_one({"id": session['uuid']}))

@app.route("/register", methods = ["POST"])
def register():
    if not User.validate_user(request.form):
        return redirect("/")

    hash_browns = bcrypt.generate_password_hash(request.form['password']) #password encryption
    dict = {
        **request.form,
        "password": hash_browns
    }

    user_id = User.create(dict)

    session["uuid"] = user_id

    return redirect('/')


@app.route("/login", methods = ["POST"])
def login():
    if not User.login_validate(request.form):
        return redirect('/')

    user = User.get_by_email({"email": request.form["email"]})

    #uuid = unique user id
    session['uuid'] = user.id

    return redirect('/users')


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")






