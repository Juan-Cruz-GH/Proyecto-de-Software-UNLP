from flask import Blueprint, render_template, request, flash, url_for, session, redirect
from src.core import usuarios


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")


@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form
    user = usuarios.find_user_by_mail_and_pass(params["email"], params["password"])
    validacion, mensaje = usuarios.validar_inputs(params["email"], params["password"])

    if not validacion:
        flash(mensaje, "error")
        return redirect(url_for("auth.login"))
    elif not user:
        flash("Credenciales invalidas", "error")
        return redirect(url_for("auth.login"))
    session["user"] = user.email
    flash("Sesión iniciada correctamente")
    return redirect(url_for("home"))

@auth_blueprint.post("/authenticated")
def authenticated(session):
    usuario = usuarios.buscar_usuario_email(session["user"])
    if not usuario:
        return None
    else: 
        return usuario

@auth_blueprint.get("/logout")
def logout():
    session.pop("user", None)
    flash("Sesión cerrada correctamente")
    return redirect(url_for("home"))
