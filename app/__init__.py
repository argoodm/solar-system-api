from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    
    # Import Routes & Register Blueprints
    from .routes import planets_bp
    app.register_blueprint(planets_bp)
    
    # from .routes import moons_bp
    # app.register_blueprint(moons_bp)

    return app
