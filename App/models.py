

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DriverCar(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    age = db.Column(db.Integer)
