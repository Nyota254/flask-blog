from flask import Flask
from config import configurations

app = Flask(__name__)

def create_app(configname):
    '''
    Method for creating the app to enable for easier configurations
    '''
    app.config.from_object(configurations[configname])
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
