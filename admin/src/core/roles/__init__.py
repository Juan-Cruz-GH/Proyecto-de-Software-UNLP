from src.core.db import db
from src.core.roles.roles import Rol


def listar_roles():
    return Rol.query.all()

def buscar_rol(rol):
    return Rol.query.filter_by(nombre=rol).first()