# app/views/__init__.py
from app.views.home import home_bp
from app.views.trends import trends_bp
from app.views.auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(trends_bp)
    app.register_blueprint(auth_bp)
