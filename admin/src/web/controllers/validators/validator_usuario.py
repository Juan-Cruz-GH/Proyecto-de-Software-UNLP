import re

def validar_inputs(email, password):
    """Esta funcion valida que los inputs sean del tipo correcto. (falta comprobar password mediante hash)"""
    regex_email = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if not (email != "" and password != ""):
        return False, "Todos los datos deben estar completos"
    elif not (re.search(regex_email, email)):
        return False, "El email debe ser valido"
    else:
        return True, "Credenciales validas"
