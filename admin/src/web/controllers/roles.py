from flask import Blueprint
from flask import render_template
from flask import request

from src.core import roles

rol_blueprint = Blueprint("roles", __name__, url_prefix="/consultas")

@rol_blueprint.get("/")
def rol_index():
    roles = roles.list_usuarios()

    return render_template("roles/index.html", roles=roles)