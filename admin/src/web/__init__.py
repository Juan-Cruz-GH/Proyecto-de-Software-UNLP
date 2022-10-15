from flask import Flask, render_template, redirect
from flask_wtf.csrf import CSRFProtect
from src.web.helpers import handlers

from src.web.controllers.usuarios import usuario_blueprint
from src.web.controllers.configuracion_sistema import configuracion_sistema_blueprint
from src.web.controllers.api import api_blueprint
from src.web.controllers.disciplinas import disciplina_blueprint
from src.web.controllers.socios import socio_blueprint
from src.web.controllers.pagos import pago_blueprint
from src.web.controllers.roles import rol_blueprint
from src.web.controllers.permisos import permiso_blueprint
from src.web.controllers.auth import auth_blueprint

from src.web.config import config
from src.core.db import db, init_db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    csrf = CSRFProtect(app)

    @app.get("/")
    def home():
        return redirect("/socios/")
        

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(configuracion_sistema_blueprint)
    app.register_blueprint(disciplina_blueprint)
    app.register_blueprint(socio_blueprint)
    app.register_blueprint(pago_blueprint)
    app.register_blueprint(rol_blueprint)
    app.register_blueprint(permiso_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(api_blueprint)
    

    with app.app_context():
        init_db(app)

    app.register_error_handler(404, handlers.not_found_error)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app