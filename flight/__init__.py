from flask import Flask, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
# from flask_mail import Mail
from flight.config import Config


# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    # db.init_app(app)
    # bcrypt.init_app(app)
    # login_manager.init_app(app)
    # mail.init_app(app)

    # from flight.route.route import register
    # from flight.route.flight import flight
    from flight.routes import flight
    app.register_blueprint(flight)
    # app.register_blueprint(register)
    # app.register_blueprint(flight)

    return app