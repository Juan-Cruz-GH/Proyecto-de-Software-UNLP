from flask import Flask, render_template
from src.web.helpers import handlers
from src.web.controllers.issues import issue_blueprint
from src.web.config import config
from src.core.db import db, init_db


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        kwargs = {"contenido": " Mundo!!"}
        return render_template("index.html", **kwargs)
        
    app.register_blueprint(issue_blueprint)

    with app.app_context():
        init_db(app)

    app.register_error_handler(404, handlers.not_found_error)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app