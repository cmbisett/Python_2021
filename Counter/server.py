from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

@app.route("/")
def index():
    session['amount'] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroySession():
    session.clear()
    session['amount'] = 0
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)