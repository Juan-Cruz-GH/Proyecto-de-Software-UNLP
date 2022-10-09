import re
from src.core.socios.socios import Socio
from src.core.db import db

def todos_los_socios(apellido=None, tipo=None):
    '''Retorna todos los socios en una lista de diccionarios'''
    data_socios = []
    if((apellido is not None) and (tipo is not None)):
        if(tipo == "true"):
            socios = Socio.query.filter_by(apellido=apellido.capitalize()).filter(Socio.activo.is_(True))
        else:
            socios = Socio.query.filter_by(apellido=apellido.capitalize()).filter(Socio.activo.is_(False))
    elif(apellido is not None):
        socios = Socio.query.filter_by(apellido=apellido.capitalize())
    elif(tipo is not None):
        if(tipo == "true"):
            socios = Socio.query.filter(Socio.activo.is_(True))
        else:
            socios = Socio.query.filter(Socio.activo.is_(False))
    else:
        socios = Socio.query.all()
    for socio in socios:
        row = socio.__dict__
        row.pop("_sa_instance_state")
        row.pop("inserted_at")
        data_socios.append(row)
    return data_socios

def listar_socios(page, apellido=None, tipo=None):
    '''Esta funcion devuelve todos los socios de forma paginada segun la configuracion
    y segun si se esta realizando un tipo de busqueda.'''
    if((apellido is not None) and (tipo is not None)):
        if(tipo == "true"):
            socios = Socio.query.filter_by(apellido=apellido.capitalize()).filter(Socio.activo.is_(True)).paginate(page, per_page=1)
        else:
            socios = Socio.query.filter_by(apellido=apellido.capitalize()).filter(Socio.activo.is_(False)).paginate(page, per_page=1)
    elif(apellido is not None):
        socios = Socio.query.filter_by(apellido=apellido.capitalize()).paginate(page, per_page=1)
    elif(tipo is not None):
        if(tipo == "true"):
            socios = Socio.query.filter(Socio.activo.is_(True)).paginate(page, per_page=1)
        else:
            socios = Socio.query.filter(Socio.activo.is_(False)).paginate(page, per_page=1)
    else:
        socios = Socio.query.paginate(page, per_page=1)
    return socios

def agregar_socio(data):
    '''Esta funcion se utiliza para dar de alta un socio'''
    socio = Socio(**data)
    db.session.add(socio)
    db.session.commit()
    return socio

def buscar_socio(id):
    '''Esta funcion busca un socio por su id'''
    socio = Socio.query.get(id)
    return socio

def modificar_socio(data):
    '''Esta funcion realiza la modificacion de los datos de un socio'''
    socio = Socio.query.get(data["id"])
    socio.nombre = data["nombre"]
    socio.apellido = data["apellido"]
    socio.email = data["email"]
    socio.tipo_documento = data["tipo_documento"]
    socio.dni = data["dni"]
    socio.genero = data["genero"]
    socio.direccion = data["direccion"]
    socio.telefono = data["telefono"]
    db.session.commit()
    return socio

def eliminar_socio(id):
    '''Esta funcion realiza la eliminacion de un socio de la BD'''
    socio = Socio.query.get(id)
    db.session.delete(socio)
    db.session.commit()

def validar_datos_existentes(dni, email, accion, id=None):
    '''Esta funcion valida que el dni o el email ingresados para dar de alta o modificar un socio no existan.
    Si el dni existe se devuelve 1, si el email existe se devuelve 2, en caso de que no exista ningun se 
    devuelve 3.'''
    if(accion == "alta"):
        dni_existente = Socio.query.filter_by(dni=dni).first()
        email_existente = Socio.query.filter_by(email=email).first()
        if(dni_existente is not None):
            return False, "El Dni ya esta cargado en el sistema."
        elif(email_existente is not None):
            return False, "El Email ya esta cargado en el sistema."
        else:
            return True, "Ambos son validos"
    elif(accion == "modificacion"):
        dni_existente = Socio.query.filter_by(dni=dni).filter(Socio.id != id).first()
        email_existente = Socio.query.filter_by(email=email).filter(Socio.id != id).first()
        if(dni_existente is not None):
            return False, "El Dni ya esta cargado en el sistema."
        elif(email_existente is not None):
            return False, "El Email ya esta cargado en el sistema."
        else:
            return True, "Ambos son validos"

def validar_inputs(data):
    '''Esta funcion valida que los inputs sean del tipo correcto.'''
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(data["nombre"] != '' and data["apellido"] != '' and data["email"] != '' and data["tipo_documento"] != '' and data["dni"] != '' and data["genero"] != '' and data["direccion"] != '' and data["genero"] != '' and data["telefono"] != ''):
        return False, "Todos los datos deben estar completos"
    elif not (data["dni"].isdigit() and data["telefono"].isdigit()):
        return False, "El telefono y dni deben ser solo numeros, sin guiones ni puntos."
    elif not(re.fullmatch(r"[A-Za-z ]{1,50}", data["nombre"]) and re.fullmatch(r"[A-Za-z ]{1,50}", data["apellido"])):
        return False, "El nombre o apellido son incorrectos."
    elif not(re.search(regex_email,data["email"])):
        return False, "El email debe ser valido"
    elif(len(data["dni"]) != 8):
        return False, "El dni debe contener 8 numeros"
    elif(len(data["telefono"]) != 10 and len(data["telefono"]) != 7):
        return False, "El numero de telefono debe tener 10 numeros si es celular y 7 si es de casa."
    else:
        return True, "Inputs Validos"