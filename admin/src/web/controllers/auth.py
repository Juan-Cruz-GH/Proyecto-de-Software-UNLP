from flask import Blueprint, render_template, request, flash, url_for, session, redirect
from werkzeug.security import generate_password_hash
from src.core import usuarios


auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_blueprint.get("/")
def login():
    return render_template("auth/login.html")

@auth_blueprint.post("/authenticate")
def authenticate():
    params = request.form

    user = usuarios.find_user_by_mail_and_pass(params["email"], generate_password_hash(params["password"], method="sha256"))
    validacion, mensaje = usuarios.validar_inputs(params["email"], params["password"])

    if not validacion:
        flash(mensaje, "error")
        return redirect(url_for("auth.login"))
    elif not user:
        flash("Credenciales invalidas", "error")
        return redirect(url_for("auth.login"))
    session["user"] = params["email"]
    flash(mensaje, "success")

    return redirect(url_for("home"))


@auth_blueprint.get("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for("home"))