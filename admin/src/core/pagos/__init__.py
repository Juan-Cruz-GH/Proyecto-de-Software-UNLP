from src.core.pagos.pagos import Pago

def listar_pagos():
    '''Esta funcion devuelve todos los pagos de un socio paginados.'''
    return Pago.query.all()