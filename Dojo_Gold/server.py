from flask import Flask, render_template, session, request, redirect
import random
from flask.wrappers import Request
app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/')
def index():
    if 'goldCount' not in session:
        session['goldCount'] = 0
    return render_template('index.html')


@app.route('/getrich', methods = ['POST'])
def getRich():
    if request.form['source'] == 'farm':
        session['goldCount'] += random.randint(10,20)
    if request.form['source'] == 'cave':
        session['goldCount'] += random.randint(5,10)
    if request.form['source'] == 'house':
        session['goldCount'] += random.randint(2,5)
    if request.form['source'] == 'casino':
        session['goldCount'] += random.randint(-50,50)

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)