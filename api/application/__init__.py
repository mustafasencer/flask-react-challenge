import datetime
import traceback
from os import environ

from flask import Flask
from flask.json import JSONEncoder, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

from api.utils.errors import AppError


def _init_error_handler(app):
    @app.errorhandler(AppError)
    def handle_app_error(e):
        return jsonify(e.__dict__), e.status

    @app.errorhandler(404)
    def resource_not_found(e):
        error = AppError(
            status=404,
            err_code='errors.brokerNotFound',
            err_msg=f'{e.description}'
        )
        return jsonify(error.__dict__), error.status

    @app.errorhandler(Exception)
    def handle_exception(e):
        error = AppError(
            status=500,
            err_code='errors.InternalServerError',
            err_msg=f'Internal Server Error. Please contact the Administrator.',
            reason=f'{traceback.format_exc()[:1000]}'
        )
        return jsonify(error.__dict__), error.status


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime.datetime):
                return obj.isoformat() + 'Z'
            if isinstance(obj, datetime.date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


limiter = Limiter(key_func=get_remote_address, default_limits=["50 per minute"])
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI',
                                                        "sqlite:///../db.sqlite3?check_same_thread=False")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 599
    app.config['HERE_API_KEY'] = environ.get("HERE_API_KEY", "GHMpZnvnc4tUxEnQ3hopDzu80UKLLXVVbt-KIoxIjdY")

    # Init modules
    CORS(app)
    db.init_app(app)
    limiter.init_app(app)
    _init_error_handler(app)
    app.json_encoder = CustomJSONEncoder

    # Routes
    from api.application import broker
    app.register_blueprint(broker.bp)

    return app
