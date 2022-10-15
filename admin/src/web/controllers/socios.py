from flask import Blueprint, render_template, request, redirect, flash
from src.core import socios
from src.core import pagos
from src import exportaciones
from src.core import disciplinas

socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")

@socio_blueprint.route("/")
def socio_index():
    '''Esta funcion llama al modulo correspondiente para obtener todos los socios paginados.'''
    page = request.args.get('page', 1, type=int)
    apellido = request.args.get('busqueda', type=str) if request.args.get('busqueda', type=str) != '' else None
    tipo = request.args.get('tipo', type=str) if request.args.get('tipo', type=str) != '' else None
    kwargs = {"socios": socios.listar_socios(page, apellido, tipo), "apellido": apellido, "tipo":tipo}
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
    validacion, mensaje = socios.validar_datos_existentes(data_socio["dni"], data_socio["email"], "alta")
    if(validacion == False):
        flash(mensaje)
        return redirect("/socios/alta-socio")
    validacion_inputs, mensaje = socios.validar_inputs(data_socio)
    if(not validacion_inputs):
        flash(mensaje)
        return redirect("/socios/alta-socio")
    socio = socios.agregar_socio(data_socio)
    generacion_pagos = pagos.generar_pagos(socio.id)
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
    validacion_datos_existentes, mensaje = socios.validar_datos_existentes(data_socio["dni"], data_socio["email"], "modificacion", data_socio["id"])
    if(not validacion_datos_existentes):
        flash(mensaje)
        return redirect("/socios/" + data_socio["id"])
    validacion_inputs, mensaje = socios.validar_inputs(data_socio)
    if(not validacion_inputs):
        flash(mensaje)
        return redirect("/socios/" + data_socio["id"])
    socio = socios.modificar_socio(data_socio)
    return redirect("/socios")

@socio_blueprint.route("/eliminar/<id>", methods=["DELETE", "GET"])
def socio_delete(id):
    '''Esta funcion llama al metodo correspondiente para eliminar un socio.'''
    socio = socios.eliminar_socio(id)
    return redirect("/socios")

@socio_blueprint.route("/exportar-csv")
def exportar_csv():
    '''Esta funcion genera un archivo CSV a partir de los datos solicitados de socios'''
    apellido = request.args.get('busqueda', type=str) if request.args.get('busqueda', type=str) != '' else None
    tipo = request.args.get('tipo', type=str) if request.args.get('tipo', type=str) != '' else None
    data_socios = socios.todos_los_socios(apellido, tipo)
    output = exportaciones.generarCSV(data_socios)
    return output

@socio_blueprint.route("/exportar-pdf")
def exportar_pdf():
    '''Esta funcion genera un archivo PDF a partir de los datos solicitados de socios'''
    apellido = request.args.get('busqueda', type=str) if request.args.get('busqueda', type=str) != '' else None
    tipo = request.args.get('tipo', type=str) if request.args.get('tipo', type=str) != '' else None
    data_socios = socios.todos_los_socios(apellido, tipo)
    output = exportaciones.generarPDF(data_socios)
    return output

@socio_blueprint.route("/inscripcion-socio/<id>")
def inscripcion_socio(id):
    '''Esta funcion retorna el formulario para la inscripcion del socio a una disciplina'''
    disciplinas2 = ['futbol', 'basquet']
    kwargs = {'id_socio': id, 'disciplinas': disciplinas.todas_las_disciplinas(), 'categorias': disciplinas.categorias_de_cada_disciplina()}
    return render_template("/socios/inscripcion_socios.html", **kwargs)

@socio_blueprint.route("/inscripcion", methods=["POST"])
def add_inscripcion():
    id_socio = request.form.get("id_socio")
    id_disciplina = request.form.get("categoria")
    socioActivo = socios.estaHabilitado(id_socio)
    disciplinaActiva = disciplinas.estaHabilitada(id_disciplina)
    if (socioActivo and disciplinaActiva):
        disciplinas.relacionarSocioDisciplina(id_disciplina, id_socio)
        return redirect("/socios/")
    else: 
        flash("La disciplina o el socio no están habilitados.")
        return redirect("/socios/inscripcion-socio/" + id_socio)