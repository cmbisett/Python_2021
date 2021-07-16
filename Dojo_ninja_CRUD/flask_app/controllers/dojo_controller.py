from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def dojo():
    context = {"all_dojos": Dojo.get_all()}
    return render_template('index.html', **context)

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/show/<int:dojo_id>')
def show_dojo(dojo_id):
    dict = {"id": dojo_id}
    return render_template('show_dojo.html', dojo = Dojo.get_one(dict))