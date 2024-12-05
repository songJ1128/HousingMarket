from flask import Flask
from app.core.config import Config
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    from app.api import housing_blueprint, auth_blueprint
    app.register_blueprint(housing_blueprint, url_prefix='/api/housing')
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

    return app
