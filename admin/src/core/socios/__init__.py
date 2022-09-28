from operator import and_
from src.core.socios.socios import Socio
from src.core.pagos.pagos import Pago
from src.core.db import db

def listar_socios(page):
    '''Esta funcion devuelve todos los socios de forma paginada segun la configuracion.'''
    return Socio.query.paginate(page, per_page=1)

def agregar_socio(data):
    '''Esta funcion se utiliza para dar de lata un socio, devolviendo 1 si ya existe un dni igual y 2 si existe un email igual ya cargado.'''
    dni_existente = Socio.query.filter_by(dni=data["dni"]).first()
    email_existente = Socio.query.filter_by(email=data["email"]).first()
    if(dni_existente is not None):
        return 1
    elif(email_existente is not None):
        return 2
    else:
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