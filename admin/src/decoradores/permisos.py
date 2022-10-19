from flask import session, redirect, url_for, abort
from src.web.helpers.permission import check_permission
from functools import wraps


def permiso_requerido(session,**kwargs):
    def permiso_decorador(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                print(kwargs)
                print(session)
                check_permission(session["user"], kwargs["tipo_permiso"])
            except KeyError:
                abort(403)
            return f(*args, *kwargs)
        return decorated_function
    return permiso_decorador
        