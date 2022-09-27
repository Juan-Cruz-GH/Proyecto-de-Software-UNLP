from src.core.pagos.pagos import Pago

def listar_pagos():
    return Pago.query.all()