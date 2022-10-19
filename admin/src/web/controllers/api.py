import json
from flask import Blueprint, session, request
from src.web.controllers import disciplinas

from src.web.controllers import configuracion_sistema
from src.web.controllers import usuarios
from src.web.controllers import pagos
from src.decoradores.login import login_requerido

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/club/info")
def obtener_info():
    """Obtiene el json con la informacion de contacto y lo retorna"""
    return configuracion_sistema.info_contacto_json()


@api_blueprint.route("/club/disciplinas")
def obtener_disciplinas():
    """Obtiene el json con todas las disciplinas y lo retorna"""
    return disciplinas.disciplina_json()


@api_blueprint.route("/auth")
def obtener_token():
    """"""
    pass


@api_blueprint.route("/me/profile")
@login_requerido
def obtener_info_usuario():
    """Obtiene el json con todos los datos del usuario logueado en este momento y lo retorna"""
    return usuarios.info_usuario_logueado()


@api_blueprint.route("/me/disciplinas")
@login_requerido
def obtener_disciplinas_usuario():
    """Obtiene el json con todas las disciplinas del usuario logueado en este momento y lo retorna"""
    pass


@api_blueprint.route("/me/payments", methods=["GET"])
def obtener_pagos():
    """Obtiene la lista de pagos registrados del usuario logueado en este momento y lo retorna"""
    return pagos.pagos_json()


@api_blueprint.route("/me/payments", methods=["POST"])
def registrar_pagos():
    """Registra un nuevo pago para el usuario logueado en este momento"""
    json = request.get_json()
    return pagos.pagar_json(json)


@api_blueprint.route("/me/license", methods=["GET"])
@login_requerido
def obtener_info_credencial():
    """Obtiene la información personal y el estado de credencial del usuario logueado en este momento y lo retorna"""
    pass
