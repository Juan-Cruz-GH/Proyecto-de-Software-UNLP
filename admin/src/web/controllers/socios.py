from flask import Blueprint, render_template, request, redirect, flash
from src.core import socios

socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")

@socio_blueprint.route("/")
def socio_index():
    '''Esta funcion llama al modulo correspondiente para obtener todos los socios paginados.'''
    page = request.args.get('page', 1, type=int)
    kwargs = {"socios": socios.listar_socios(page)}
    return render_template("socios/index.html", **kwargs)

@socio_blueprint.route("/alta-socio")
def form_socio():
    '''Esta funcion devuelve el template con un formulario para dar de alta un usuario'''
    return render_template("socios/alta_socios.html")

@socio_blueprint.route("/<id>")
def socio_profile(id):
    '''Esta funcion llama al modulo correspondiente para obtener a un socio por su id.'''
    kwargs = {"socio": socios.buscar_socio(id)}
    return render_template("socios/perfil_socio.html", **kwargs)

@socio_blueprint.route("/alta", methods=["POST"])
def socio_add():
    '''Esta funcion llama al metodo correspondiente para dar de alta un socio. 
    Si recibe un 1 es porque ese dni ya esta cargado, si devuelve un 2 es porque ese mail ya esta cargado.'''
    data_socio = {
        "nombre": request.form.get("nombre").capitalize(),
        "apellido": request.form.get("apellido").capitalize(),
        "email": request.form.get("email"),
        "activo": True,
        "tipo_documento": request.form.get("tipo_documento"),
        "dni": request.form.get("documento"),
        "genero": request.form.get("genero"),
        "direccion": request.form.get("direccion"),
        "telefono": request.form.get("telefono"),
    }
    socio = socios.agregar_socio(data_socio)
    if(socio == 1):
        flash("El Dni ya esta cargado en el sistema")
        return redirect("/socios/alta-socio")
    elif(socio == 2):
        flash("El Email ya esta cargado en el sistema")
        return redirect("/socios/alta-socio")
    #generacion_pagos = pagos.generar_pagos(socio.id)
    return redirect("/socios")

@socio_blueprint.route("/modificacion", methods=["POST"])
def socio_update():
    '''Esta funcion llama al metodo correspondiente para modificar los datos de un socio.'''
    data_socio = {
        "id": request.form.get("id"),
        "nombre": request.form.get("nombre").capitalize(),
        "apellido": request.form.get("apellido").capitalize(),
        "email": request.form.get("email"),
        "activo": True,
        "tipo_documento": request.form.get("tipo_documento"),
        "dni": request.form.get("documento"),
        "genero": request.form.get("genero"),
        "direccion": request.form.get("direccion"),
        "telefono": request.form.get("telefono"),
    }
    socio = socios.modificar_socio(data_socio)
    return redirect("/socios")

@socio_blueprint.route("/eliminar/<id>", methods=["POST", "GET"])
def socio_delete(id):
    '''Esta funcion llama al metodo correspondiente para eliminar un socio.'''
    socio = socios.eliminar_socio(id)
    return redirect("/socios")