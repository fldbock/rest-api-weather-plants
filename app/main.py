from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load the configuration
    app.config.from_envvar('APP_CONFIG_FILE')

    # Initialize the flask_sqlalchemy extension with flask
    db.init_app(app)

    # Register routes
    from app.routes import register_routes
    register_routes(app, db)

    # Initializes the flask_migrate extension with flask
    Migrate(app, db)

    return app



    

