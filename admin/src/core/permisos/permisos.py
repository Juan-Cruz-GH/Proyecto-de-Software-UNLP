from src.core.db import db

class Permiso(db.model):
    __tablename__ = "Permisos"
    id=db.column(db.Integer, primary_key=True, nullable=False, unique=True)
    nombre= db.column(db.String(100), nullable=False)

