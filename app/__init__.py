from flask import Flask
from flask_login import LoginManager
from config import config
from extensions import db

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    
    from .auth.routes import auth
    
    app.register_blueprint(auth) 
    
    return app