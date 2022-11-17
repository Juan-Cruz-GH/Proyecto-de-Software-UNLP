from flask import Flask, redirect, request
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_cors import CORS

from src.web.controllers.usuarios import usuario_blueprint
from src.web.controllers.configuracion_sistema import configuracion_sistema_blueprint
from src.web.controllers.api import api_blueprint
from src.web.controllers.disciplinas import disciplina_blueprint
from src.web.controllers.socios import socio_blueprint
from src.web.controllers.pagos import pago_blueprint
from src.web.controllers.auth import auth_blueprint
from src.decoradores.login import login_requerido
from src.web.helpers import handlers
from src.web.helpers.permission import has_permission
from src.web.config import config
from src.core.db import db, init_db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    csrf = CSRFProtect(app)
    CORS(app)
    csrf.exempt(api_blueprint)

    @app.after_request
    def after_request(response):
        white_origin= ['https://grupo23.proyecto2022.linti.unlp.edu.ar']
        if request.headers['Origin'] in white_origin:
            response.headers['Access-Control-Allow-Origin'] = request.headers['Origin'] 
            response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        return response

    @app.get("/")
    @login_requerido
    def home():
        return redirect("/socios/")

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(configuracion_sistema_blueprint)
    app.register_blueprint(disciplina_blueprint)
    app.register_blueprint(socio_blueprint)
    app.register_blueprint(pago_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_blueprint)

    Session(app)

    with app.app_context():
        init_db(app)

    app.register_error_handler(401, handlers.not_authenticated_error)
    app.register_error_handler(403, handlers.not_authorized_error)
    app.register_error_handler(404, handlers.not_found_error)

    app.jinja_env.globals.update(permiso=has_permission)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app
