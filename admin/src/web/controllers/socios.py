from flask import Blueprint, render_template
from src.core import socios

socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")

@socio_blueprint.get("/")
def socio_index():
    kwargs = {"socios": socios.listar_socios()}
    return render_template("socios/index.html", **kwargs)