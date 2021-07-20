from os import name
from flask import Flask, render_template, session, request, redirect
from flask.wrappers import Request
from werkzeug.utils import redirect
from models.dojo import Dojo


app = Flask(__name__)
app.secret_key = "keep it secret , keep it safe"

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def result():
    if not Dojo.validate(request.form):
        return redirect('/')

    last_id = Dojo.create(request.form)
    return redirect(f"/results/{last_id}")
    
    return redirect('/results')

@app.route('/results/<int:id>')
def results(id):
    dict = {"id": id}
    return render_template('results.html', dojo_id = Dojo.get_one(dict))



if __name__=="__main__":
    app.run(debug=True)