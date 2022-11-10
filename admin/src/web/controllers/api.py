from flask import Blueprint, make_response, request

from src.web.controllers import disciplinas
from src.web.controllers import configuracion_sistema
from src.web.controllers import pagos
from src.web.controllers.validators import validator_api

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/club/disciplinas", methods=["GET"])
def obtener_disciplinas():
    """Obtiene el json con todas las disciplinas y lo retorna"""
    respuesta = make_response(disciplinas.disciplina_json(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.route("/me/disciplinas", methods=["GET"])
def obtener_disciplinas_socio():
    # no enviar header, viaja el JWT, no se pregunta sobre otro socio
    """Valida el header id y devuelve la respuesta en formato json"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_disciplinas_socio(id)
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.route("/me/license", methods=["GET"])
def obtener_info_y_estado_socio():
    # no enviar header, viaja el JWT, no se pregunta sobre otro socio
    """Obtiene la información personal y el estado de credencial del socio enviado en el request y lo retorna"""
    id = request.headers.get("id")
    mensaje, http_code = validator_api.validar_header_estado_socio(id)
    respuesta = make_response(mensaje, http_code)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.route("/me/payments", methods=["GET"])
def obtener_pagos():
    """Obtiene la lista de pagos registrados del usuario logueado en este momento y lo retorna"""
    return pagos.pagos_json()


@api_blueprint.route("/me/payments", methods=["POST"])
def registrar_pagos():
    """Registra un nuevo pago para el usuario logueado en este momento"""
    return pagos.pagar_json(request.get_json())


@api_blueprint.route("/club/info", methods=["GET"])
def obtener_info_club():
    """Obtiene el json con la informacion de contacto y lo retorna"""
    return configuracion_sistema.info_contacto_json()


@api_blueprint.route("/auth", methods=["POST"])
def obtener_token():
    """"""
    pass


@api_blueprint.route("/me/profile", methods=["GET"])
def obtener_info_usuario():
    # no enviar header, viaja el JWT, no se pregunta sobre otro socio
    """Obtiene el json con todos los datos del usuario que se envia por parametro y lo retorna"""
    pass
