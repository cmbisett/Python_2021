from flask import Flask, render_template, redirect, request # Import Flask to allow us to create our app
from flask_app import app
from flask_app.models.email import Email



@app.route('/')
def index():
    return render_template("index.html")


@app.route("/register", methods = ['POST'])
def email():
    if not Email.validate(request.form):
        return redirect("/")
    
    Email.create(request.form)
    return redirect("/success")


@app.route("/success")
def success():
    return render_template("success.html", email_list = Email.get_all())