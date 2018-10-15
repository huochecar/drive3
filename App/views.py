from flask import Blueprint, render_template

from App.models import DriverCar

blue = Blueprint('blue',__name__)

@blue.route('/')
def hello():
    return '123'
@blue.route('/get/')
def get():
    animals = DriverCar.query.all()
    return render_template('get.html',animals=animals)

