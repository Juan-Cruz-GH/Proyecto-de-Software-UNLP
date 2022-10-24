from functools import wraps

from flask import abort

from src.web.helpers.permission import check_permission


def permiso_requerido(session, tipo_permiso):
    def permiso_decorador(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                print(session["user"])
                print(tipo_permiso)
                check_permission(session["user"], tipo_permiso)
            except KeyError:
                abort(403)
            return f(*args, **kwargs)

        return decorated_function

    return permiso_decorador
