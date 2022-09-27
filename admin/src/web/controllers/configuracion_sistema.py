from flask import Blueprint, render_template
from src.core import configuracion_sistema


configuracion_sistema_blueprint=Blueprint("configuracion_sistema",__name__, url_prefix="/configuracion_del_sistema")

@configuracion_sistema.get("/")
def configuracion_index():
    kwargs = {"config": configuracion_sistema.getPaginado()}
    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)