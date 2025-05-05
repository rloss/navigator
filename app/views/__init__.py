from app.views.home import home_bp
from app.views.trends import trends_bp

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(trends_bp)
    # 여기에 다른 bp들 추가하면 됨
