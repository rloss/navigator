from app.views.home import home_bp
from app.views.trends import trends_bp
from app.views.strategies import strategies_bp
from app.views.mypage import mypage_bp
from app.views.mypage_edit import mypage_edit_bp
from app.views.my_strategies import my_strategies_bp
from app.views.auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(trends_bp)
    app.register_blueprint(strategies_bp)
    app.register_blueprint(mypage_bp)
    app.register_blueprint(mypage_edit_bp)
    app.register_blueprint(my_strategies_bp)
    app.register_blueprint(auth_bp)
