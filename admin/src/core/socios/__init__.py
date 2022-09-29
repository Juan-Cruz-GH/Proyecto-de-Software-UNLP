from src.core.socios.socios import Socio
from src.core.db import db

def listar_socios(page):
    '''Esta funcion devuelve todos los socios de forma paginada segun la configuracion.'''
    return Socio.query.paginate(page, per_page=1)

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