from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from flask import Blueprint, render_template
from src.core import configuracion_sistema
from src.core.db import db
from flask import request


configuracion_sistema_blueprint=Blueprint("configuracion_sistema",__name__, url_prefix="/configuracion_del_sistema")

@configuracion_sistema_blueprint.get("/")
def configuracion_index():
    kwargs = {"pageconfig": configuracion_sistema.getPaginado()}
    
    #configuracion_sistema.getConfiguracionGeneral()
    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)

@configuracion_sistema_blueprint.route("/update", methods =["POST"])
def configuracion_actualizar():
    configuraciones ={
            "elementos_pagina": request.form.get("elementos_pagina"),
        }
    config_paginado= Configuracion_paginado(**configuraciones)
    db.session.add(config_paginado)
    db.session.commit()