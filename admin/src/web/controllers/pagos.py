from flask import Blueprint, render_template, request, session
from src.core import pagos
from src.decoradores.login import login_requerido
from src.core import usuarios

pago_blueprint = Blueprint("pagos", __name__, url_prefix="/pagos")


@pago_blueprint.route("/")
@login_requerido
def pagos_index():
    """Esta funcion llama al modulo pagos para listar todos los socios"""
    kwargs = {
        "pagos": pagos.listar_pagos(),
        "usuario": usuarios.buscar_socio_email(session["user"]),
    }
    return render_template("socios/pagos.html", **kwargs)


@pago_blueprint.route("/socioPagos/<id>/")
@login_requerido
def pagos_socios(id):
    """Esta funcion retorna todos los pagos asociados al socio solicitado"""
    page = request.args.get("page", 1, type=int)
    kwargs = {
        "pagos": pagos.listar_pagos_socio(id, page),
        "id_socio": id,
        "usuario": usuarios.buscar_socio_email(session["user"]),
    }
    return render_template("pagos/pagos_socio.html", **kwargs)
