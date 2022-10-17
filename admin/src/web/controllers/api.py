from flask import Blueprint
from src.web.controllers import disciplinas
from src.web.controllers import configuracion_sistema
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
    """"""
    pass


@api_blueprint.route("/me/disciplinas")
@login_requerido
def obtener_disciplinas_usuario():
    """Obtiene el json con todas las disciplinas del usuario autenticado y lo retorna"""
    pass


@api_blueprint.route("/me/payments", methods=["GET"])
@login_requerido
def obtener_pagos():
    """"""
    pass


@api_blueprint.route("/me/payments", methods=["POST"])
@login_requerido
def registrar_pagos():
    """"""
    pass


@api_blueprint.route("/me/license", methods=["GET"])
@login_requerido
def obtener_info_credencial():
    """"""
    pass
