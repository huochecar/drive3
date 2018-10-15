from flask_migrate import Migrate
from flask_session import Session

from App.models import db
from App.views import blue


def init_ext(app):
    app.config['SECRET_KEY'] = '110'
    Session(app=app)
    app.register_blueprint(blueprint=blue)
    db.init_app(app=app)
    migrate = Migrate()
    migrate.init_app(app=app,db=db)