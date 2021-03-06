import os
from flask import Flask
from instance.config import app_config
from .API.v1.views.user_views import users_v1    
from .API.v1.views.questions_views import questions_v1    

def create_app(config_name="development"):
    """ Set up the application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])
    app.url_map.strict_slashes = False
    app.register_blueprint(users_v1)
    app = Flask(__name__)
    app.config.from_object(app_config["development"])
    
    app.register_blueprint(users_v1)
    app.register_blueprint(questions_v1)

    return app

