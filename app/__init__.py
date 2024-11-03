from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        # Import parts of our application
        from . import routes
        
        # Create the database if it doesn't exist
        db.create_all()

    return app
