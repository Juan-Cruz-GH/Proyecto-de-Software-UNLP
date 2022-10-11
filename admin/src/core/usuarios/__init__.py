from src.core.db import db
from src.core.usuarios.usuarios import Usuario
import re


def listar_usuarios(page):
    '''Esta funcion devuelve todos los usuarios de forma paginada segun la configuracion.'''
    return Usuario.query.paginate(page, per_page=1)


def agregar_usuario(data):
    '''Esta funcion se utiliza para dar de alta un usuario'''
    usuario = Usuario(**data)
    db.session.add(usuario)
    db.session.commit()

    return usuario


def buscar_usuario(id):
    '''Esta funcion busca un usuario por su id'''
    usuario = Usuario.query.get(id)
    return usuario


def find_user_by_mail_and_pass(email, password):
    '''esta funcion verifica que el usuario ingresado en login exista'''
    return Usuario.query.filter(Usuario.email == email, Usuario.password == password).first()


def validar_inputs(email, password):
    '''Esta funcion valida que los inputs sean del tipo correcto. (falta comprobar password mediante hash)'''
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not(email != '' and password != ''):
        return False, "Todos los datos deben estar completos"
    elif not(re.search(regex_email, email)):
        return False, "El email debe ser valido"
    else:
        return True, "Credenciales validas"


def validar_datos_existentes(email, username, accion, id=None):
    '''Esta funcion valida que el dni o el email ingresados para dar de alta o modificar un usuario no existan.
    Si el dni existe se devuelve 1, si el email existe se devuelve 2, en caso de que no exista ningun se 
    devuelve 3.'''
    if(accion == "alta"):
        email_existente = Usuario.query.filter_by(email=email).first()
        username_existente = Usuario.query.filter_by(username=username).first()
        if(email_existente is not None):
            return False, "El Email ya esta cargado en el sistema."
        elif(username_existente is not None):
            return False, "El Nombre de Usuario ya esta cargado en el sistema"
        else:
            return True, "Ambos son validos"
    elif(accion == "modificacion"):
        email_existente = Usuario.query.filter_by(email=email).filter(Usuario.id != id).first()
        username_existente = Usuario.query.filter_by(username=username).filter(Usuario.id != id).first()
        if(email_existente is not None):
            return False, "El Email ya esta cargado en el sistema."
        elif(username_existente is not None):
            return False, "El Nombre de Usuario ya esta cargado en el sistema."
        else:
            return True, "Ambos son validos"


def modificar_usuario(data):
    '''Esta funcion realiza la modificacion de los datos de un usuario'''
    usuario = Usuario.query.get(data["id"])
    usuario.nombre = data["nombre"]
    usuario.apellido = data["apellido"]
    usuario.email = data["email"]
    usuario.username = data["username"]
    db.session.commit()
    return usuario


def eliminar_usuario(id):
    '''Esta funcion realiza la eliminacion de un usuario de la BD'''
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()

