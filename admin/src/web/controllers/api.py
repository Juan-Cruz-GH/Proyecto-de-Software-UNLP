from flask import Blueprint
from src.web.controllers import disciplinas
from src.web.controllers import configuracion_sistema

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/club/info")  # No requiere auth
def obtener_info():
    '''Obtiene el json con la informacion de contacto y lo retorna'''
    return configuracion_sistema.info_contacto_json()

@api_blueprint.route("/club/disciplinas") # No requiere auth
def obtener_disciplinas():
    '''Obtiene el json con todas las disciplinas y lo retorna'''
    return disciplinas.disciplina_json()

@api_blueprint.route("/auth") # No requiere auth
def obtener_token():
    ''''''
    pass

@api_blueprint.route("/me/profile") # Requiere auth
def obtener_info_usuario():
    ''''''
    pass


@api_blueprint.route("/me/disciplinas") # Requiere auth
def obtener_disciplinas_usuario():
    '''Obtiene el json con todas las disciplinas del usuario autenticado y lo retorna'''
    pass  

@api_blueprint.route("/me/payments", methods=["GET"]) # Requiere auth
def obtener_pagos():
    ''''''
    pass

@api_blueprint.route("/me/payments", methods=["POST"]) # Requiere auth
def registrar_pagos():
    ''''''
    pass

@api_blueprint.route("/me/license", methods=["GET"])   # Requiere auth
def obtener_info_credencial():
    ''''''
    pass





