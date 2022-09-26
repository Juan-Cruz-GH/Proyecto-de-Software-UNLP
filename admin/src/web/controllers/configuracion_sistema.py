from flask import Blueprint, render_template


configuracion_sistema=Blueprint("configuracion_sistema",__name__, url_prefix="/configuracion_del_sistema")

@configuracion_sistema.get("/")
def configuracion_index():
    kwargs = {"config"}
    return render_template("configuracion_sistema/configuracion_sistema.html")