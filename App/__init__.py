from flask import Flask

from App import settings
from App.ext import init_ext

def create_app(ENV_NAME):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(ENV_NAME))
    init_ext(app)



    return app