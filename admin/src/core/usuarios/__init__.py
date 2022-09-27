from src.core.db import db
from src.core.usuarios.usuarios import Usuario

def list_usuarios():
    return Usuario.query.all()

def create_usuario(**kwargs):
    usuario = Usuario(**kwargs)
    db.session.add(Usuario)
    db.session.commit()

    return usuario