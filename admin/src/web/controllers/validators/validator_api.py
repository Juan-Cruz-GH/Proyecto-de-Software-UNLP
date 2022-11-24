from src.web.controllers import socios
from src.web.controllers import pagos


def validar_general(id):
    if id is None:
        return {"Error": "No se envió el header id."}, 400
    if not (id.isdigit()):
        return {"Error": "El header id enviado no es un numero."}, 400
    if not socios.existe_socio(id):
        return {"Error": "El socio no existe."}, 404


def validar_header_disciplinas_socio(id):
    error = validar_general(id)
    if error is None:
        return socios.disciplinas_socio(id), 200
    return error


def validar_header_estado_socio(id):
    error = validar_general(id)
    if error is None:
        return socios.json_estado_socio(id), 200
    return error


def validar_header_pagos_socio(id):
    error = validar_general(id)
    if error is None:
        return pagos.pagos_json(id), 200
    return error
