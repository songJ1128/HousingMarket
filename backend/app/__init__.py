from flask import Flask
from app.core.config import Config
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    # Register Blueprints
    #from app.api.routes import api_blueprint
    #app.register_blueprint(api_blueprint)

    return app
