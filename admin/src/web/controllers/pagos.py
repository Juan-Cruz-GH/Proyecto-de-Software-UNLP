from flask import Blueprint, render_template
from src.core import pagos

pago_blueprint = Blueprint("pagos", __name__, url_prefix="/pagos")

@pago_blueprint.get("/")
def pagos_index():
    '''Esta funcion llama al modulo pagos para listar todos los socios'''
    kwargs = {"pagos": pagos.listar_pagos()}
    return render_template("socios/pagos.html", **kwargs)