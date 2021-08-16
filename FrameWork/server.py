from flask_app import app

from flask_app.controllers import user_controller #import controllers to use the route for each controller


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
