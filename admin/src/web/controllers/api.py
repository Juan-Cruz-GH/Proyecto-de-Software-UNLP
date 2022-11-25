from flask import Blueprint, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.web.controllers import disciplinas
from src.web.controllers import socios
from src.web.controllers import configuracion_sistema
from src.web.controllers import pagos
from src.web.controllers.validators import validator_api

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.get("/club/disciplinas")
def obtener_disciplinas():
    """Retorna un json con todas las disciplinas que se practican en el club"""
    respuesta = make_response(disciplinas.disciplina_json(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/club/socios-años")
def socios_por_año():
    """Retorna un json con la cantidad de socios por año"""
    respuesta = make_response(socios.socios_por_año(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/club/socios-genero")
def socios_genero():
    """Retorna un json con la cantidad de socios por genero"""
    respuesta = make_response(socios.socios_genero(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/club/socios-disciplinas")
def obtener_socios_disciplinas():
    """Retorna un json con los socios por disciplinas"""
    respuesta = make_response(disciplinas.disciplinas_socios(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/club/info")
def obtener_info_club():
    """Retorna el json con la información de contacto del club"""
    respuesta = make_response(configuracion_sistema.info_contacto_json(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/disciplinas")
@jwt_required()
def obtener_disciplinas_socio():
    """Retorna el json con todas las disciplinas que realiza
    el socio que está logueado actualmente en la app pública (JWT)"""
    mensaje, http_code = validator_api.validar_header_disciplinas_socio(
        str(get_jwt_identity())
    )
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/license")
@jwt_required()
def obtener_info_y_estado_socio():
    """Retorna el json con el estado de credencial y los datos
    del socio que está logueado actualmente en la app pública (JWT)"""
    mensaje, http_code = validator_api.validar_header_estado_socio(str(get_jwt_identity()))
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/profile")
@jwt_required()
def obtener_info_socio():
    """Retorna el json con todos los datos
    del socio que está logueado actualmente en la app pública (JWT)"""
    pass


@api_blueprint.get("/me/payments")
@jwt_required()
def obtener_pagos_socio():
    """Retorna la lista de pagos registrados
    del socio que está logueado actualmente en la app pública (JWT)"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_pagos_socio(str(get_jwt_identity()))
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/pending_payments")
@jwt_required()
def obtener_pagos_adeudados_socio():
    """Retorna la lista de pagos adeudados
    del socio que está logueado actualmente en la app pública (JWT)"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_pagos_socio(str(get_jwt_identity()))
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.post("/me/payments")
@jwt_required()
def registrar_pago_socio():
    """Registra un nuevo pago para
    el socio que está logueado actualmente en la app pública (JWT)"""
    return pagos.pagar_json(request.get_json(), get_jwt_identity())


@api_blueprint.post("/auth")
def obtener_token():
    """Recibe un json con user y password y retorna su JWT, lo realiza el login publico por ahora"""
    pass
