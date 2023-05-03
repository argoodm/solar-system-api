# Configure the database to use SQLAlchemy 
# it will contain the application factory, create_app
# python treats app directory as a package.

# import packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# set up variables for database operations
db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'    
    
    # abby's table
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planets_development'
    
    # import model
    from app.models.planet import Planet
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import Routes & Register Blueprints
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    # return the app
    return app
