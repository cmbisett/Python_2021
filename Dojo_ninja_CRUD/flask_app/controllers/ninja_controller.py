from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninja")
def create_ninja():
    context = {"all_dojos": Dojo.get_all()}
    return render_template('create_ninja.html', **context)

@app.route("/ninja/create", methods=["POST"])
def create_ninja_info():
    Ninja.create(request.form)
    dojo_id = request.form["dojo_id"]
    return redirect(f"/show/{dojo_id}")