from flask import Blueprint

light_bp = Blueprint('light', __name__, url_prefix='/light')
music_bp = Blueprint('music', __name__, url_prefix='/music')
sensor_bp = Blueprint('sensor', __name__, url_prefix='')
weather_bp = Blueprint('weather', __name__, url_prefix='/weather')
emotion_bp = Blueprint('emotion', __name__, url_prefix='/emotion')
system_bp = Blueprint('system', __name__, url_prefix='')

from routes import light_routes, music_routes, sensor_routes, weather_routes, emotion_routes, system_routes

def register_routes(app):
    app.register_blueprint(light_bp)
    app.register_blueprint(music_bp)
    app.register_blueprint(sensor_bp)
    app.register_blueprint(weather_bp)
    app.register_blueprint(emotion_bp)
    app.register_blueprint(system_bp)