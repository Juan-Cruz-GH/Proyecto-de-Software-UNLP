from src.core.db import db
from src.core.permisos.permisos import Permiso


def listar_permisos():
    return Permiso.query.all()
