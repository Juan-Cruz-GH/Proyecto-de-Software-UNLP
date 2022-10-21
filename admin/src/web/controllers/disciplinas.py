from flask import Blueprint, render_template, request, redirect, flash, session, abort
from src.core import disciplinas
from src.core import usuarios
from src.web.controllers.validators import validator_disciplinas
from src.web.helpers.permission import check_permission
from src.decoradores.login import login_requerido
import json

disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")


def disciplina_json():
    """Retorna el json con todas las disciplinas"""
    return json.dumps(disciplinas.listar_disciplinas_diccionario())


@disciplina_blueprint.route("/")
@login_requerido
def disciplina_index():
    """Muestra las disciplinas de la página indicada en el request. Si no hay request, la página será la primera"""
    if check_permission(session["user"], "disciplina_index"):
        page = request.args.get("page", 1, type=int)
        kwargs = {
            "disciplinas": disciplinas.listar_disciplinas(page),
            "usuario": usuarios.buscar_usuario_email(session["user"]),
        }
        return render_template("disciplinas/index.html", **kwargs)
    else:
        return abort(403)


@disciplina_blueprint.route("/alta-disciplina")
@login_requerido
def form_disciplina():
    """Devuelve el template con el formulario para agregar una disciplina"""
    if check_permission(session["user"], "disciplina_new"):
        kwargs = {"usuario": usuarios.buscar_usuario_email(session["user"])}
        return render_template("disciplinas/alta_disciplinas.html", **kwargs)
    else:
        return abort(403)


@disciplina_blueprint.route("/<id>")
@login_requerido
def disciplina_profile(id):
    """Busca una disciplina por el id indicado en la URL y devuelve el template con el formulario para modificar una disciplina"""
    kwargs = {
        "disciplina": disciplinas.buscar_disciplina(id),
        "usuario": usuarios.buscar_usuario_email(session["user"]),
    }
    return render_template("disciplinas/perfil_disciplinas.html", **kwargs)


@disciplina_blueprint.route("/alta", methods=["POST"])
@login_requerido
def disciplina_add():
    """Llama a las funciones del modelo para validar los inputs del formulario para agregar una disciplina. Si los inputs son validos, le dice al modelo que la agregue"""
    data_disciplina = {
        "nombre": request.form.get("nombre").capitalize(),
        "categoria": request.form.get("categoria").capitalize(),
        "instructores": request.form.get("instructores"),
        "horarios": request.form.get("horarios"),
        "costo": request.form.get("costo"),
        "habilitada": (request.form.get("habilitada") == "Si"),
    }
    resultado, mensaje = validator_disciplinas.validar_inputs(data_disciplina)
    if resultado:
        resultado, mensaje = disciplinas.validar_disciplina_repetida(
            data_disciplina["nombre"], data_disciplina["categoria"], "alta"
        )
        if resultado:
            disciplinas.agregar_disciplina(data_disciplina)
            return redirect("/disciplinas")
        else:
            flash(mensaje)
            return redirect("/disciplinas/alta-disciplina")
    else:
        flash(mensaje)
        return redirect("/disciplinas/alta-disciplina")


@disciplina_blueprint.route("/modificacion", methods=["POST"])
@login_requerido
def disciplina_update():
    """Llama a las funciones del modelo para validar los inputs del formulario para modificar una disciplina. Si los inputs son validos, le dice al modelo que la modifique"""
    if check_permission(session["user"], "disciplina_update"):
        data_disciplina = {
            "id": request.form.get("id"),
            "nombre": request.form.get("nombre").capitalize(),
            "categoria": request.form.get("categoria").capitalize(),
            "instructores": request.form.get("instructores"),
            "horarios": request.form.get("horarios"),
            "costo": request.form.get("costo"),
            "habilitada": (request.form.get("habilitada") == "Si"),
        }
        resultado, mensaje = validator_disciplinas.validar_inputs(data_disciplina)
        if resultado:
            resultado, mensaje = disciplinas.validar_disciplina_repetida(
                data_disciplina["nombre"],
                data_disciplina["categoria"],
                "modificacion",
                data_disciplina["id"],
            )
            if resultado:
                disciplinas.modificar_disciplina(data_disciplina)
                return redirect("/disciplinas")
            else:
                flash(mensaje)
                return redirect("/disciplinas/" + data_disciplina["id"])
        else:
            flash(mensaje)
            return redirect("/disciplinas/" + data_disciplina["id"])
    else:
        return abort(403)


@disciplina_blueprint.route("/eliminar/<id>", methods=["DELETE", "GET"])
@login_requerido
def disciplina_delete(id):
    """Le dice al modelo que borre la disciplina enviada"""
    if check_permission(session["user"], "disciplina_destroy"):
        disciplinas.eliminar_disciplina(id)
        return redirect("/disciplinas")
    else:
        return abort(403)
