from flask import Blueprint, render_template
from src.core import configuracion_sistema


configuracion_sistema_blueprint=Blueprint("configuracion_sistema",__name__, url_prefix="/configuracion_del_sistema")

@configuracion_sistema_blueprint.get("/")
def configuracion_index():
    kwargs = {"pageconfig": configuracion_sistema.getPaginado()}
    kwargs2= {"generalconfig":configuracion_sistema.getConfiguracionGeneral()}
    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)