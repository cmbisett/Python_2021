from os import name
from flask import Flask, render_template, session, request, redirect
from flask.wrappers import Request
from werkzeug.utils import redirect
app = Flask(__name__)
app.secret_key = "keep it secret , keep it safe"

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def result():
    print(request.form)
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['languages'] = request.form['languages']
    session['comments'] = request.form['comments']
    
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)