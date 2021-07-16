from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app import app



@app.route('/')
def index():
    # context = {"all_users": User.get_all()}
    # return render_template("index.html", **context)
    return render_template("index.html", all_users = User.get_all())

# DISPLAYS THE FORM FOR CREATING A USER
@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/users/created', methods = ["POST"])
def retrieve_form():
    User.create(request.form)
    return redirect('/')


@app.route('/users/<int:user_id>')
def get_one(user_id):
    #dict = {'id': user_id}
    # return render_template('singleUser.html', user = User.get_one({dict}))
    return render_template('singleUser.html', user = User.get_one({'id': user_id}))


@app.route('/edit/<int:user_id>')
def edit_User(user_id):
    return render_template('edit_user.html', user = User.get_one({'id': user_id}))


@app.route('/users/<int:user_id>/update', methods = ["POST"])
def updated_users(user_id):
    another_dict = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": user_id
    }
    # print(another_dict)
    # User.update(request.form)
    User.update(another_dict)

    return redirect('/')


@app.route('/user/<int:user_id>/delete')
def delet_user(user_id):
    another_dict = {
        **request.form,
        "id": user_id
    }
    User.delete(another_dict)

    return redirect('/')