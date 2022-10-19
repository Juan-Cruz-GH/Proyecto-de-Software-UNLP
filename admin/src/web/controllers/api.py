from flask import Blueprint, make_response
from src.web.controllers import disciplinas
from src.web.controllers import configuracion_sistema
from src.web.controllers import usuarios
from src.decoradores.login import login_requerido

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/club/disciplinas", methods=["GET"])  # 1er entrega
def obtener_disciplinas():
    """Obtiene el json con todas las disciplinas y lo retorna"""
    respuesta = make_response(disciplinas.disciplina_json(), 200)
    respuesta.headers["Content-Type"] = "application/json"
    return respuesta


@api_blueprint.route("/me/disciplinas", methods=["GET"])  # 1er entrega
def obtener_disciplinas_usuario(id):
    """Obtiene el json con todas las disciplinas del usuario que se envia por parametro y lo retorna"""
    pass


@api_blueprint.route("/me/payments", methods=["GET"])  # 1er entrega
def obtener_pagos():
    """Obtiene la lista de pagos registrados del usuario logueado en este momento y lo retorna"""
    pass


@api_blueprint.route("/me/payments", methods=["POST"])  # 1er entrega
def registrar_pagos():
    """Registra un nuevo pago para el usuario logueado en este momento"""
    pass


@api_blueprint.route("/me/profile", methods=["GET"])  # 2da entrega
def obtener_info_usuario(id):
    """Obtiene el json con todos los datos del usuario que se envia por parametro y lo retorna"""
    return usuarios.info_usuario_logueado()


@api_blueprint.route("/auth", methods=["POST"])  # 2da entrega
def obtener_token():
    """"""
    pass


@api_blueprint.route("/me/license", methods=["GET"])  # 2da entrega
def obtener_info_credencial():
    """Obtiene la información personal y el estado de credencial del usuario logueado en este momento y lo retorna"""
    pass


@api_blueprint.route("/club/info", methods=["GET"])  # 2da entrega
def obtener_info():
    """Obtiene el json con la informacion de contacto y lo retorna"""
    return configuracion_sistema.info_contacto_json()
