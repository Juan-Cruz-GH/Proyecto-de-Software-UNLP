from flask import Blueprint, render_template


permiso_blueprint = Blueprint("permisos", __name__, url_prefix="/consultas")


@permiso_blueprint.get("/")
def permiso_index():
    permisos = permisos.list_usuarios()

    return render_template("permisos/index.html", permisos=permisos)
