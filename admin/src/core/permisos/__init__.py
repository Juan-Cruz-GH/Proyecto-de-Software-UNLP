from src.core.db import db
from src.core.permisos.permisos import Permiso


def listar_permisos():
    return Permiso.query.all()

def buscar_permiso(permiso):
    """buscar un objeto permiso, segun el nombre que llego por parametro"""
    return Permiso.query.filter_by(nombre = permiso).first()