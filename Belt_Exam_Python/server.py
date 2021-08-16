from flask_app import app
from flask_app.controllers import sighting_controller, user_controller #import controllers to use the routes for each controller


if __name__=="__main__":      
    app.run(debug=True)    
