from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    print(type(name))
    return f"Hi! {name}"

@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    print(type(num))
    return name * num







if __name__=="__main__":
    app.run(debug=True)