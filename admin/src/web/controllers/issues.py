from flask import Blueprint, render_template
from src.core.board.issue import Issue

issue_blueprint = Blueprint("issues", __name__, url_prefix="/consultas")

@issue_blueprint.get("/")
def issue_index():

    issue = Issue()
    kwargs = {"issues": issue.getAll()}
    return render_template("issues/index.html", **kwargs)