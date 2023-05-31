from . import db
from .models import Data
from flask import render_template, redirect, url_for, request, session, Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return redirect(url_for('main.index'))


@main.route('/home')
def index():
    return render_template('index.html')


@main.route('/devices', methods=['GET'])
@login_required
def devices():
    return render_template('device.html', login=current_user.login)


@main.route('/devices/station', methods=['GET'])
def station():
    return render_template('station.html')


@main.route('/devices/security', methods=['GET'])
@login_required
def security():
    return render_template('device_security.html')


@main.route('/devices/weatherStation', methods=['GET'])
@login_required
def weatherStation():
    return render_template('device_weatherStation.html')


@main.route('/devices/greenhouse', methods=['GET'])
@login_required
def greenhouse():
    return render_template('device_greenhouse.html')


# Ппереписать, очень сильно плохо (
@main.route('/devices/greenhouse/getTemperature', methods=['GET'])
@login_required
def get_temperature():
    temp = Data.query.order_by(Data.id.desc()).first().temperature
    return f"{temp}°C", 200


@main.route('/devices/greenhouse/getPressure', methods=['GET'])
@login_required
def get_pressure():
    hum = Data.query.order_by(Data.id.desc()).first().pressure
    return f"{hum}Па", 200
