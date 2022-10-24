from enum import unique
from src.core.db import db
from datetime import datetime

from src.core.db import db


class Socio(db.Model):
    __tablename__ = "Socios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    apellido = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
    tipo_documento = db.Column(db.String, nullable=False)
    dni = db.Column(db.String, unique=True, nullable=False)
    genero = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    telefono = db.Column(db.String, nullable=False)
    pagos = db.relationship("Pago", back_populates="socio")
    inserted_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(
        self,
        nombre,
        apellido,
        email,
        tipo_documento,
        dni,
        genero,
        direccion,
        telefono,
        activo=True,
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.activo = activo
        self.tipo_documento = tipo_documento
        self.dni = dni
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono

    def __repr__(self):
        return (
            f"Socio(id={self.id!r}, nombre={self.nombre!r}, apellido={self.apellido!r})"
        )
