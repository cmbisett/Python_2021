from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello!'

# @app.route('/play')
# def play():
#     return render_template('index.html')

# @app.route('/play/<int:x>')
# def addBoxes(x):
#     return render_template('index.html', x=x)

# @app.route('/play/<int:x>/<string:color>')
# def add_color(x, color):
#     return render_template('index.html', x=x, color=color)



#adding multiple URLs to a function
@app.route('/')
@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def add_color(x=3, color='blue'): #have default values for the paramiters so it doesnt break when a URL doesnt need parameters
    return render_template('index.html', x=x, color=color)


if __name__=="__main__":
    app.run(debug=True)