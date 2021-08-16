from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/users')
def users():
    users = [
    {
        'first_name' : 'Cameron', 
        'last_name' : 'Bisett',
        'full_name' : 'Cameron Bisett',
    },
    {
        'first_name' : 'Taylor', 
        'last_name' : 'Bisett',
        'full_name' : 'Taylor Bisett',
    },
    {
        'first_name' : 'Summer', 
        'last_name' : 'Bisett',
        'full_name' : 'Summer Bisett',
    },
    {
        'first_name' : 'Steve', 
        'last_name' : 'Bisett',
        'full_name' : 'Steve Bisett',
    }
]
    return render_template("index.html", users = users)

    
if __name__ == "__main__":
    app.run(debug=True)