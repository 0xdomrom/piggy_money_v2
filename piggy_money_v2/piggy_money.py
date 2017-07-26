from flask import Flask
from werkzeug.utils import find_modules, import_string


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)

    app.config.update(dict())

    #app.config.from_envvar('PIGGY_MONEY_SETTINGS', silent=False)
    register_blueprints(app)

    return app

    
def register_blueprints(app):
    for name in find_modules('piggy_money_v2.blueprints'):
        module = import_string(name)
        if hasattr(module, 'bp'):
            app.register_blueprint(module.bp)
