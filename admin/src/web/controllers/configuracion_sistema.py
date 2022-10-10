from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from flask import Blueprint, render_template
from src.core import configuracion_sistema
from src.core.db import db
from flask import request, redirect


configuracion_sistema_blueprint=Blueprint("configuracion_sistema",__name__, url_prefix="/configuracion_del_sistema")

@configuracion_sistema_blueprint.get("/")
def configuracion_index():
    paginado = {"paginado": configuracion_sistema.getPaginado()}
    config = {"config": configuracion_sistema.getConfiguracionGeneral()}
    if (config["config"].activar_pagos==True):
        config["config"].activar_pagos="checked"
    else:
        config["config"].activar_pagos=""
    kwargs = {**paginado,** config}
    
    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)

@configuracion_sistema_blueprint.route("/update", methods =["POST"])
def configuracion_actualizar():

    paginado={
        "elementos_pagina": request.form.get("elementos_pagina"),
    }
    configuraciones ={
        "activar_pagos":request.form.get("activar_pagos"),
        "encabezado_recibos":request.form.get("encabezado_recibos"),
        "informacion_contacto": request.form.get("informacion_contacto"),
        "cuota_base": request.form.get("cuota_base"),
        "porcentaje_recargo": request.form.get("porcentaje_recargo")
    }

    if (configuraciones["activar_pagos"]== "pagos activados"):
        configuraciones["activar_pagos"] = True
    else:
        configuraciones["activar_pagos"]= False

    config= configuracion_sistema.modificar_configuracion(configuraciones, paginado)
    return redirect("/configuracion_del_sistema/")
