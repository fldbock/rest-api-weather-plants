from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import LocalConfig, TestConfig

db = SQLAlchemy()

def create_app(env: str):
    app = Flask(__name__)
    
    # Load the configuration
    app.config.from_object(LocalConfig)

    if env == 'test':
        app.config.from_object(TestConfig)

    # Initialize DB
    db.init_app(app)
    

    # Register routes
    from app.routes import register_routes
    register_routes(app, db)

    # Migrate the DB
    migrate = Migrate(app, db)

    return app



    

