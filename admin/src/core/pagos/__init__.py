from src.core.pagos.pagos import Pago
from datetime import datetime
from src.core.db import db

def generar_pagos(id_socio):
    '''Esta funcion genera los cuotas a pagar por el socio cuando se lo da de alta.'''
    año_acutal = str(datetime.now().year)
    fecha_ingreso = datetime.now().date()
    fecha_diciembre = datetime.strptime("30/12/" + año_acutal, "%d/%m/%Y").date()
    cuotas = int((fecha_diciembre.year - fecha_ingreso.year) * 12 + (fecha_diciembre.month - fecha_ingreso.month))
    desde = 12 - cuotas
    for i in range(desde, 13):
        data_pago = {
            "total": 0,
            "fecha_pago": datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
            "socio_id": id_socio,
            "nro_cuota": i,
            "estado": False,
        }
        pago = Pago(**data_pago)
        db.session.add(pago)
        db.session.commit()

def listar_pagos_socio(id, page):
    '''Esta funcion realiza la consulta para obtener los pagos del socio recibido'''
    pagos = Pago.query.filter_by(socio_id=id).paginate(page, per_page=1)
    return pagos