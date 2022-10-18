from flask import Blueprint, render_template, request

from src.core import configuracion_sistema
from src.exportaciones import generarReciboPDF
from src.core import socios
from src.core import pagos


pago_blueprint = Blueprint("pagos", __name__, url_prefix="/pagos")


@pago_blueprint.route("/")
def pagos_index():
    """Esta funcion llama al modulo pagos para listar todos los socios"""
    kwargs = {"pagos": pagos.listar_pagos()}
    return render_template("socios/pagos.html", **kwargs)


@pago_blueprint.route("/socioPagos/<id>/")
def pagos_socios(id):
    """Esta funcion retorna todos los pagos asociados al socio solicitado"""
    page = request.args.get("page", 1, type=int)
    kwargs = {"pagos": pagos.listar_pagos_socio(id, page), "id_socio": id}
    return render_template("pagos/pagos_socio.html", **kwargs)


@pago_blueprint.route("/pago_de_cuota/<id>")
def pagar_cuota(id):
    """Paso de confirmacion antes de cambiar el estado de una cuota impaga a pagada"""
    pago = pagos.get_cuota(id)
    if pago.estado == True:
        return pagos_socios(pago.socio.id)
    socio = socios.buscar_socio(pago.socio.id)
    if pago.total == 0:
        total = pagos.calcular_cuota(pago.id, pago.socio.id)
    else:
        total = pago.total
    kwargs = {"pago": pago, "total": total}
    return render_template("pagos/pago_de_cuota.html", **kwargs)


@pago_blueprint.route("/pago_confirmado/<id>")
def confirmar_pago(id):
    """Cambia el estado de una cuota de impaga a pagada. Persiste la fecha y monto de pago en la base de datos"""
    pago = pagos.get_cuota(id)
    if pago.estado == False:
        pagos.pagar_cuota(id, pago.socio.id)
    return pagos_socios(pago.socio.id)


@pago_blueprint.route("/descargar_pdf_recibo/<id>")
def generarRecibo(id):
    """Descarga un recibo en pdf para una cuota pagada"""
    data_pago = {
        "encabezado": configuracion_sistema.getConfiguracionGeneral().encabezado_recibos,
        "pago": pagos.get_cuota(id),
    }
    if data_pago["pago"].estado == True:
        output = generarReciboPDF(data_pago)
        return output
    else:
        return pagos_socios(data_pago["pago"].socio.id)
