from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    login_manager.init_app(app)

    # Імпорт та реєстрація блакитних принтів
    from app.routes.user_routes import user_bp
    from app.routes.api_routes import api_bp
    from app.routes.admin_routes import admin_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
