import csv
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, flash
from src.core import socios
from src.core import pagos
from src.utils import PDF

socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")

@socio_blueprint.route("/")
def socio_index():
    '''Esta funcion llama al modulo correspondiente para obtener todos los socios paginados.'''
    page = request.args.get('page', 1, type=int)
    apellido = request.args.get('busqueda', type=str)
    tipo = request.args.get('tipo', type=str)
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
    validacion_inputs, mensaje = socios.validar_inputs(data_socio)
    if(validacion == False):
        flash(mensaje)
        return redirect("/socios/alta-socio")
    elif(not validacion_inputs):
        flash(mensaje)
        return redirect("/socios/alta-socio")
    else:
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
    validacion_inputs, mensaje = socios.validar_inputs(data_socio)
    if(not validacion_datos_existentes):
        flash(mensaje)
        return redirect("/socios/" + data_socio["id"])
    elif(not validacion_inputs):
        flash(mensaje)
        return redirect("/socios/" + data_socio["id"])
    else:
        socio = socios.modificar_socio(data_socio)
    return redirect("/socios")

@socio_blueprint.route("/eliminar/<id>", methods=["POST", "GET"])
def socio_delete(id):
    '''Esta funcion llama al metodo correspondiente para eliminar un socio.'''
    socio = socios.eliminar_socio(id)
    return redirect("/socios")

@socio_blueprint.route("/exportar-csv")
def exportar_csv():
    data_socios = socios.todos_los_socios()
    headers = ['id', 'apellido', 'activo', 'dni', 'genero', 'telefono', 'nombre', 'email', 'tipo_documento', 'direccion']
    with open('socios.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_socios)
    return redirect('/socios')

@socio_blueprint.route("/exportar-pdf")
def exportar_pdf():
    data_socios = socios.todos_los_socios()
    pdf = PDF()
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 20, f'{datetime.now().date()}')
    pdf.set_font('Arial', 'B', 12)
    y_height = 5
    pdf.set_xy(0, 50)
    pdf.cell(15)
    pdf.cell(30, y_height, 'Nombre', border=1)
    pdf.cell(30, y_height, 'Apellido', border=1)
    pdf.cell(25, y_height, 'Dni', border=1)
    pdf.cell(25, y_height, 'Telefono', border=1)
    pdf.cell(30, y_height, 'Genero', border=1)
    pdf.cell(40, y_height, 'Direccion', border=1, ln=1)
    pdf.set_font('Arial', '', 12)
    for socio in data_socios:
        pdf.cell(5)
        pdf.cell(30, y_height, socio["nombre"], border=1)
        pdf.cell(30, y_height, socio["apellido"], border=1)
        pdf.cell(25, y_height, socio["dni"], border=1)
        pdf.cell(25, y_height, socio["telefono"], border=1)
        pdf.cell(30, y_height, socio["genero"], border=1)
        pdf.cell(40, y_height, socio["direccion"], border=1, ln=1)
    pdf.output('listado_socios.pdf', 'F')
    return redirect('/socios')