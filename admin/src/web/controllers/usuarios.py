from flask import Blueprint
from flask import render_template
from flask import request

from src.core import usuarios

usuario_blueprint = Blueprint("usuarios", __name__, url_prefix="/consultas")

@usuario_blueprint.get("/")
def usuario_index():
    usuarios = usuarios.list.usuarios()

    return render_template("usuarios/index.html", usuarios=usuarios)