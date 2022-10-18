from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from flask import Blueprint, render_template, session
from src.core import configuracion_sistema
from src.core.db import db
from flask import request, redirect, flash
from src.decoradores.login import login_requerido
from src.core import usuarios
import json


configuracion_sistema_blueprint = Blueprint(
    "configuracion_sistema", __name__, url_prefix="/configuracion_del_sistema"
)


def info_contacto_json():
    """Retorna el json con todas las disciplinas"""
    return json.dumps(configuracion_sistema.get_info_contacto_diccionario())


@configuracion_sistema_blueprint.get("/")
@login_requerido
def configuracion_index():
    paginado = {"paginado": configuracion_sistema.get_paginado()}
    config = {"config": configuracion_sistema.get_configuracion_general()}
    if config["config"] == None or paginado["paginado"] == None:
        configuracion_sistema.configuracion_predeterminada()
        paginado = {"paginado": configuracion_sistema.get_paginado()}
        config = {"config": configuracion_sistema.get_configuracion_general()}

    if config["config"].activar_pagos == True:
        config["config"].activar_pagos = "checked"
    else:
        config["config"].activar_pagos = ""
    kwargs = {**paginado, **config}

    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)


@configuracion_sistema_blueprint.route("/update", methods=["POST"])
@login_requerido
def configuracion_actualizar():

    paginado = {
        "elementos_pagina": request.form.get("elementos_pagina"),
    }
    configuraciones = {
        "activar_pagos": request.form.get("activar_pagos"),
        "encabezado_recibos": request.form.get("encabezado_recibos"),
        "informacion_contacto": request.form.get("informacion_contacto"),
        "cuota_base": request.form.get("cuota_base"),
        "porcentaje_recargo": request.form.get("porcentaje_recargo"),
    }

    # Sanitizar datos
    if configuraciones["activar_pagos"] == "pagos activados":
        configuraciones["activar_pagos"] = True
    else:
        configuraciones["activar_pagos"] = False
    validar = True
    hubo_error = False
    validar, mensaje = configuracion_sistema.validar_digito(
        paginado["elementos_pagina"]
    )
    if not validar:
        flash("Elementos por página: " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_digito(
        configuraciones["cuota_base"]
    )
    if not validar:
        flash("El valor de la cuota " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_digito(
        configuraciones["porcentaje_recargo"]
    )
    if not validar:
        flash("El valor de porcentaje de recargo " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_positivo(
        configuraciones["porcentaje_recargo"]
    )
    if not validar:
        flash("El valor de porcentaje de recargo " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_positivo(
        configuraciones["cuota_base"]
    )
    if not validar:
        flash("El valor de la cuota " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_cadena(
        configuraciones["informacion_contacto"]
    )
    if not validar:
        flash("Informacion de contacto: " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_cadena(
        configuraciones["encabezado_recibos"]
    )
    if not validar:
        flash("Encabezado de los recibos: " + mensaje)
        hubo_error = True

    if hubo_error:
        return redirect("/configuracion_del_sistema/")

    config = configuracion_sistema.modificar_configuracion(configuraciones, paginado)
    return redirect("/configuracion_del_sistema/")
