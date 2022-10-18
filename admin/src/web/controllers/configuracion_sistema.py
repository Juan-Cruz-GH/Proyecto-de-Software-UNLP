from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from flask import Blueprint, render_template
from src.core import configuracion_sistema
from src.core.db import db
from flask import request, redirect, flash


configuracion_sistema_blueprint = Blueprint(
    "configuracion_sistema", __name__, url_prefix="/configuracion_del_sistema"
)


@configuracion_sistema_blueprint.get("/")
def configuracion_index():
    paginado = {"paginado": configuracion_sistema.getPaginado()}
    configuracion = {"config": configuracion_sistema.getConfiguracionGeneral()}
    if configuracion["config"] == None or paginado["paginado"] == None:
        configuracion_sistema.configuracionPredeterminada()
        paginado = {"paginado": configuracion_sistema.getPaginado()}
        configuracion = {"config": configuracion_sistema.getConfiguracionGeneral()}

    if configuracion["config"].activar_pagos == True:
        configuracion["config"].activar_pagos = "checked"
    else:
        configuracion["config"].activar_pagos = ""
    kwargs = {**paginado, **configuracion}

    return render_template("configuracion_sistema/configuracion_sistema.html", **kwargs)


@configuracion_sistema_blueprint.route("/update", methods=["POST"])
def configuracion_actualizar():

    paginado = {
        "elementos_pagina": request.form.get("elementos_pagina"),
    }
    configuracion = {
        "activar_pagos": request.form.get("activar_pagos"),
        "encabezado_recibos": request.form.get("encabezado_recibos"),
        "informacion_contacto": request.form.get("informacion_contacto"),
        "cuota_base": request.form.get("cuota_base"),
        "porcentaje_recargo": request.form.get("porcentaje_recargo"),
    }

    # Sanitizar datos
    if configuracion["activar_pagos"] == "pagos activados":
        configuracion["activar_pagos"] = True
    else:
        configuracion["activar_pagos"] = False
    validar = True
    hubo_error = False
    validar, mensaje = configuracion_sistema.validar_digito(
        paginado["elementos_pagina"]
    )
    if not validar:
        flash("Elementos por página: " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_digito(configuracion["cuota_base"])
    if not validar:
        flash("El valor de la cuota " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_digito(
        configuracion["porcentaje_recargo"]
    )
    if not validar:
        flash("El valor de porcentaje de recargo " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_positivo(
        configuracion["porcentaje_recargo"]
    )
    if not validar:
        flash("El valor de porcentaje de recargo " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_positivo(
        configuracion["cuota_base"]
    )
    if not validar:
        flash("El valor de la cuota " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_cadena(
        configuracion["informacion_contacto"]
    )
    if not validar:
        flash("Informacion de contacto: " + mensaje)
        hubo_error = True

    validar, mensaje = configuracion_sistema.validar_cadena(
        configuracion["encabezado_recibos"]
    )
    if not validar:
        flash("Encabezado de los recibos: " + mensaje)
        hubo_error = True

    if hubo_error:
        return redirect("/configuracion_del_sistema/")

    config = configuracion_sistema.modificar_configuracion(configuracion, paginado)
    return redirect("/configuracion_del_sistema/")
