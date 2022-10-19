from src.core import socios
from src.core import configuracion_sistema
from src.core.pagos.pagos import Pago
from src.core import disciplinas
from datetime import datetime, date
from src.core.db import db
from src.core import configuracion_sistema


def get_cuota(id):
    """Busca una cuota por id"""
    return Pago.query.get(id)


def generar_pagos(id_socio):
    """Esta funcion genera los cuotas a pagar por el socio cuando se lo da de alta."""
    año_actual = str(datetime.now().year)
    fecha_ingreso = datetime.now().date()
    fecha_diciembre = datetime.strptime("30/12/" + año_actual, "%d/%m/%Y").date()
    cuotas = int(
        (fecha_diciembre.year - fecha_ingreso.year) * 12
        + (fecha_diciembre.month - fecha_ingreso.month)
    )
    desde = 12 - cuotas
    for i in range(desde, 13):
        data_pago = {
            "total": 0,
            "socio_id": id_socio,
            "nro_cuota": i,
            "estado": False,
        }
        pago = Pago(**data_pago)
        db.session.add(pago)
        db.session.commit()


def listar_pagos_socio(id, page):
    """Esta funcion realiza la consulta para obtener los pagos del socio recibido"""
    pagos = Pago.query.filter_by(socio_id=id).paginate(
        page, per_page=configuracion_sistema.get_paginado().elementos_pagina
    )

    for pago in pagos.items:
        if not pago.estado or pago.total == 0:
            pago.total = calcular_cuota(pago.id, id)
    return pagos


def pagar_cuota(id_pago, id_socio):
    """Cambia el estado de una cuota la cual pasa de impaga a paga"""
    cuota = get_cuota(id_pago)
    if cuota.total == 0:
        cuota.total = calcular_cuota(id_pago, id_socio)
    cuota.fecha_pago = datetime.now()
    cuota.estado = True
    db.session.commit()


def calcular_cuota(id_pago, id_socio):
    """
    Calcula el valor de una cuota teniendo en cuenta cuota base,
    costo de cada disciplina del socio y si la cuota esta vencida
    """
    cuota = configuracion_sistema.get_configuracion_general().cuota_base
    recargo = configuracion_sistema.get_configuracion_general().porcentaje_recargo
    socio = socios.buscar_socio(id_socio)

    for disciplina in socio.disciplinas:
        cuota = cuota + int(disciplina.costo)
    if cuota_esta_vencida(id_pago):
        cuota = cuota + ((cuota * recargo) / 100)
    return cuota


def cuota_esta_vencida(id_pago):
    """Devuelve verdadero si el pago esta vencido y falso en caso contrario"""
    cuota = get_cuota(id_pago)
    vencimiento = date(int(cuota.año_cuota), int(cuota.nro_cuota), 10)
    return vencimiento < datetime.now().date()
