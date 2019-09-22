from flask import Flask
from config import configurations
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(configname):
    '''
    Method for creating the app to enable for easier configurations
    '''
    app.config.from_object(configurations[configname])

    #Importing BluePrints
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    #Initialising the Importations
    db.init_app(app)
    bootstrap.init_app(app)

    return app
