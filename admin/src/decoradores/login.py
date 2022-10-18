from flask import session, redirect, url_for
from functools import wraps


#def login_requerido(f):
#    @wraps(f)
#    def decorated_function(*args, **kwargs):
#        try:
#            session["user"]
#        except KeyError:
#            return redirect(url_for("auth.login"))
#        return f(*args, **kwargs)
#
#    return decorated_function
