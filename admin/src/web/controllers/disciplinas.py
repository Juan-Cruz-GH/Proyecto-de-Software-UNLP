from flask import Blueprint, render_template, request, redirect, flash
from src.core import disciplinas

disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplina_blueprint.route("/")
def disciplina_index():
    page = request.args.get('page', 1, type = int)
    kwargs = {"disciplinas" : disciplinas.listar_disciplinas(page)}
    return render_template("disciplinas/index.html", **kwargs)

@disciplina_blueprint.route("/alta-disciplina")
def form_disciplina():
    return render_template("disciplinas/alta_disciplinas.html")

@disciplina_blueprint.route("/<id>")
def disciplina_profile(id):
    kwargs = {"disciplina" : disciplinas.buscar_disciplina(id)}
    return render_template("disciplinas/perfil_disciplinas.html", **kwargs)

@disciplina_blueprint.route("/alta", methods=["POST"])
def disciplina_add():
    data_disciplina = {
        "nombre": request.form.get("nombre").capitalize(),
        "categoria": request.form.get("categoria").capitalize(),
        "instructores": request.form.get("instructores"),
        "horarios": request.form.get("horarios"),
        "costo": request.form.get("costo"),
        "habilitada": True
    }
    #Hay que agregar validaciones a costo (no puede tener letras), nombre (no puede tener numeros) 
    disciplinas.agregar_disciplina(data_disciplina)
    return redirect("/disciplinas")


@disciplina_blueprint.route("/modificacion", methods=["POST"])
def disciplina_update():
    data_disciplina = {
        "id": request.form.get("id"),
        "nombre": request.form.get("nombre").capitalize(),
        "categoria": request.form.get("categoria").capitalize(),
        "instructores": request.form.get("instructores"),
        "horarios": request.form.get("horarios"),
        "costo": request.form.get("costo"),
        "habilitada": True
    }
    #Hay que agregar validaciones a costo (no puede tener letras), nombre (no puede tener numeros)
    disciplinas.modificar_disciplina(data_disciplina) 
    return redirect("/disciplinas")

@disciplina_blueprint.route("/eliminar/<id>", methods=["POST", "GET"])
def disciplina_delete(id):
    disciplinas.eliminar_disciplina(id)
    return redirect("/disciplinas")