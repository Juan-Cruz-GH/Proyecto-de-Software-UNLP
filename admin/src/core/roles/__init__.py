from src.core.db import db
from src.core.roles.roles import Rol


def listar_roles():
    return Rol.query.all()
