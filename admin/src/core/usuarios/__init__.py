from src.core.db import db
from src.core.usuarios.usuarios import Usuario
import re

def list_usuarios():
    return Usuario.query.all()

def create_usuario(**kwargs):
    usuario = Usuario(**kwargs)
    db.session.add(Usuario)
    db.session.commit()

    return usuario

def find_user_by_mail_and_pass(email, password):
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
