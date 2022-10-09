from flask import Blueprint, render_template, request, redirect, flash
from src.core import disciplinas

disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplina_blueprint.route("/")
def disciplina_index():
    '''Muestra las disciplinas de la página indicada en el request. Si no hay request, la página será la primera'''
    page = request.args.get('page', 1, type=int)
    kwargs = {"disciplinas" : disciplinas.listar_disciplinas(page)}
    return render_template("disciplinas/index.html", **kwargs)

@disciplina_blueprint.route("/alta-disciplina")
def form_disciplina():
    '''Devuelve el template con el formulario para agregar una disciplina'''
    return render_template("disciplinas/alta_disciplinas.html")

@disciplina_blueprint.route("/<id>")
def disciplina_profile(id):
    '''Busca una disciplina por el id indicado en la URL y devuelve el template con el formulario para modificar una disciplina'''
    kwargs = {"disciplina" : disciplinas.buscar_disciplina(id)}
    return render_template("disciplinas/perfil_disciplinas.html", **kwargs)

@disciplina_blueprint.route("/alta", methods=["POST"])
def disciplina_add():
    '''Llama a las funciones del modelo para validar los inputs del formulario para agregar una disciplina. Si los inputs son validos, le dice al modelo que la agregue'''
    data_disciplina = {
        "nombre": request.form.get("nombre").capitalize(),
        "categoria": request.form.get("categoria").capitalize(),
        "instructores": request.form.get("instructores"),
        "horarios": request.form.get("horarios"),
        "costo": request.form.get("costo"),
        "habilitada": request.form.get("habilitada")
    }
    resultado, mensaje = disciplinas.validar_inputs(data_disciplina)
    if(resultado):
        resultado, mensaje = disciplinas.validar_disciplina_repetida(data_disciplina["nombre"], "alta", data_disciplina["id"])
        if(resultado):
            disciplinas.agregar_disciplina(data_disciplina)
            return redirect("/disciplinas")
        else:
            flash(mensaje)
            return redirect("/disciplinas/alta-disciplina") 
    else:
        flash(mensaje)
        return redirect("/disciplinas/alta-disciplina")

@disciplina_blueprint.route("/modificacion", methods=["POST"])
def disciplina_update():
    '''Llama a las funciones del modelo para validar los inputs del formulario para modificar una disciplina. Si los inputs son validos, le dice al modelo que la modifique'''
    data_disciplina = {
        "id": request.form.get("id"),
        "nombre": request.form.get("nombre").capitalize(),
        "categoria": request.form.get("categoria").capitalize(),
        "instructores": request.form.get("instructores"),
        "horarios": request.form.get("horarios"),
        "costo": request.form.get("costo"),
        "habilitada": request.form.get("habilitada")
    }
    resultado, mensaje = disciplinas.validar_inputs(data_disciplina)
    if(resultado):
        resultado, mensaje = disciplinas.validar_disciplina_repetida(data_disciplina["nombre"], "modificacion", data_disciplina["id"])
        if(resultado):
            disciplinas.modificar_disciplina(data_disciplina)
            return redirect("/disciplinas")
        else:
            flash(mensaje)
            return redirect("/disciplina" + data_disciplina["id"]) 
    else:
        flash(mensaje)
        return redirect("/disciplinas" + data_disciplina["id"])

@disciplina_blueprint.route("/eliminar/<id>", methods=["POST", "GET"])
def disciplina_delete(id):
    '''Le dice al modelo que borre la disciplina enviada'''
    disciplinas.eliminar_disciplina(id)
    return redirect("/disciplinas")