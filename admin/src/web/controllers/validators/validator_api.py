from src.web.controllers import socios


def validar_header_disciplinas_socio(id):
    if id is None:
        return {"Error": "No se envió el header id."}, 400
    if not (id.isdigit()):
        return {"Error": "El header id enviado no es un numero."}, 400
    if not socios.existe_socio(id):
        return {"Error": "El socio no existe."}, 404
    return socios.disciplinas_socio(id), 200


def validar_header_estado_socio(id):
    if id is None:
        return {"Error": "No se envió el header id."}, 400
    if not (id.isdigit()):
        return {"Error": "El header id enviado no es un numero."}, 400
    if not socios.existe_socio(id):
        return {"Error": "El socio no existe."}, 404
    return socios.json_estado_socio(id), 200
