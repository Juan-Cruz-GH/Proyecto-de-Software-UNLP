from flask import session, abort
from functools import wraps


def login_requerido(f):
    '''Esta decorador es utilizado para verificar si hay una sesion existente del usuario'''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            session["user"]
        except KeyError:
            abort(401)
        return f(*args, **kwargs)

    return decorated_function
