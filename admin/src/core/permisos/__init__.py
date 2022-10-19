from src.core.db import db
from src.core.permisos.permisos import Permiso


def listar_permisos():
    '''Esta funcion lista los permisos disponibles'''
    return Permiso.query.all()
