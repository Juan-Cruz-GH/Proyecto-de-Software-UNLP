from flask import Blueprint, make_response, request

from src.web.controllers import disciplinas
from src.web.controllers import configuracion_sistema
from src.web.controllers import pagos
from src.web.controllers.validators import validator_api
from flask_cors import cross_origin

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.get("/club/disciplinas")
@cross_origin
def obtener_disciplinas():
    """Retorna un json con todas las disciplinas que se practican en el club"""
    respuesta = make_response(disciplinas.disciplina_json(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/disciplinas")
def obtener_disciplinas_socio():
    """Retorna el json con todas las disciplinas que realiza
    el socio que está logueado actualmente en la app pública (JWT)"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_disciplinas_socio(id)
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/license")
def obtener_info_y_estado_socio():
    """Retorna el json con el estado de credencial y los datos
    del socio que está logueado actualmente en la app pública (JWT)"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_estado_socio(id)
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.get("/me/profile")
def obtener_info_socio():
    """Retorna el json con todos los datos
    del socio que está logueado actualmente en la app pública (JWT)"""
    pass


@api_blueprint.get("/me/payments")
def obtener_pagos_socio():
    """Retorna la lista de pagos registrados
    del socio que está logueado actualmente en la app pública (JWT)"""
    return pagos.pagos_json()


@api_blueprint.post("/me/payments")
def registrar_pago_socio():
    """Registra un nuevo pago para
    el socio que está logueado actualmente en la app pública (JWT)"""
    return pagos.pagar_json(request.get_json())


@api_blueprint.get("/club/info")
@cross_origin
def obtener_info_club():
    """Retorna el json con la información de contacto del club"""
    return configuracion_sistema.info_contacto_json()


@api_blueprint.post("/auth")
def obtener_token():
    """Recibe un json con user y password y retorna su JWT"""
    pass
