from flask import Blueprint, request, jsonify, make_response
from src.core import socios
from src.web.controllers.socios import json_informacion_socio
from src.web.controllers.validators import validator_usuario

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
)
from flask_jwt_extended import unset_jwt_cookies, jwt_required
from flask_jwt_extended import get_jwt_identity

auth_publico_blueprint = Blueprint("auth_publico", __name__, url_prefix="/auth_publico")


@auth_publico_blueprint.post("/login_publico")
def login_publico():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    validacion, mensaje = validator_usuario.validar_inputs_publico(email, password)
    if not validacion:
        return jsonify(message=mensaje), 400

    socio = socios.find_socio_by_email_and_pass(email, password)

    if socio:
        access_token = create_access_token(identity=socio.id)
        response = jsonify(access_token)
        set_access_cookies(response, access_token)
        return response, 201
    else:
        return jsonify(message="Credenciales Invalidas"), 400


@auth_publico_blueprint.get("/logout_publico")
@jwt_required()
def logout_publico():
    response = jsonify()
    unset_jwt_cookies(response)
    return response, 200


@auth_publico_blueprint.get("/socio_jwt")
@jwt_required()
def socio_jwt():
    socio_actual = get_jwt_identity()
    response = make_response(json_informacion_socio(socio_actual))
    return response, 200
