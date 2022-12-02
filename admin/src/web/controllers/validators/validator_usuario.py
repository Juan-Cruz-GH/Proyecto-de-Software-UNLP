import re

from src.web.controllers.validators.common_validators import is_none


def validate_name_fields_are_null(nombre, apellido):
    if is_none(nombre):
        return True, "El campo nombre  no puede ser nulo"
    if is_none(apellido):
        return True, "El campo apellido  no puede ser nulo"
    return False, "Los campos no son nulo"


def validar_inputs(email, password, data_rol):
    """Esta funcion valida que los inputs sean del tipo correcto."""
    regex_email = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if not (email != "" and password != ""):
        return False, "Todos los datos deben estar completos"
    elif not (re.search(regex_email, email)):
        return False, "El email debe ser valido"
    elif data_rol["ROL_ADMINISTRADOR"] is None and data_rol["ROL_OPERADOR"] is None:
        return False, "Se debe seleccionar un rol"
    else:
        return True, "Credenciales validas"


def validar_inputs_publico(email, password):
    """Esta funcion valida que los inputs del login publico sean del tipo correcto"""
    regex_email = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if not (email != "" and password != ""):
        return False, "Todos los datos deben estar completos"
    elif not (re.search(regex_email, email)):
        return False, "El email debe ser valido"
    else:
        return True, "Credenciales validas"
