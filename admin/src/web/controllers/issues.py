from flask import Blueprint, render_template
from src.core import board

issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")

@issue_blueprint.get("/")
def issue_index():
    kwargs = {"issues": board.list_issues()}
    return render_template("issues/index.html", **kwargs)