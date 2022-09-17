from flask import Flask, render_template
from src.web.helpers import handlers
from src.web.controllers.issues import issue_blueprint
from src.web.config import config

def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    @app.get("/")
    def home():
        kwargs = {"contenido": " Mundo!!"}
        return render_template("index.html", **kwargs)
        
    app.register_blueprint(issue_blueprint)

    app.register_error_handler(404, handlers.not_found_error) 
    return app