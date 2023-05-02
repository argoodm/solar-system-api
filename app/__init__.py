from flask import Flask
from flask_sql_alchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
def create_app(test_config=None):
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'

    db.init_app(app)
    migrate.init_app(app, db)
    # Import Routes & Register Blueprints
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    from app.models.planets import Planet
    # from .routes import moons_bp
    # app.register_blueprint(moons_bp)

    return app
