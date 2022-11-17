from flask import Blueprint, request, jsonify, abort
from src.core import socios

from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from flask_jwt_extended import unset_jwt_cookies, jwt_required
from flask_jwt_extended import get_jwt_identity

auth_publico_blueprint = Blueprint("auth_publico", __name__, url_prefix="/auth_publico")

@auth_publico_blueprint.post("/login_publico")
def login_publico():
    data = request.get_json()
    email = data['email']
    password = data['password']
    socio = socios.find_socio_by_email_and_pass(email, password)

    if socio: 
        access_token = create_access_token(identity=socio.id)
        response = jsonify()
        set_access_cookies(response, access_token)
        return response, 200
    else:
        return jsonify(message='Sin autorizacion'), 401
"""respuesta del post aprobado 201 y mala 400"""

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
    socio = socio.buscar_socio(socio_actual)
    response = jsonify(socio)
    return response, 200