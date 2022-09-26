from src.core.db import db
from datetime import datetime

Socio_Disciplina=db.Table(
    "Socio_Disciplina",
    db.column("id_socio", db.Integer, db.ForeignKey(Socios.id), nullable=False),
    db.column("id_disciplina", db.Integer, db.ForeignKey(Disciplinas.id), nullable=False)
)

class Disciplina(db.Model):
    __tablename__ = "Disciplinas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    nombre_instructor = db.Column(db.String(30), nullable=False)
    apellido_instructor = db.Column(db.String(40), nullable=False)
    dias = db.Column(db.String, nullable=False)
    horarios = db.Column(db.String, nullable=False)
    costo = db.Column(db.String, nullable=False)
    habilitada = db.Column(db.Boolean, nullable=False)
    inserted_at = db.Column(db.DateTime, default=datetime.now())

    socios = db.relationship("Socio", secondary=Socio_Disciplina)

    def __init__(self, nombre=None, categoria=None, nombre_instructor=None, apellido_instructor=None,
    dias=None, horarios=None, costo=None, habilitada=None):
        self.nombre = nombre
        self.categoria = categoria
        self.nombre_instructor = nombre_instructor
        self.apellido_instructor = apellido_instructor
        self.dias = dias
        self.horarios = horarios
        self.costo = costo
        self.habilitada = habilitada

    def __repr__(self):
        return f"Disciplina (id={self.id!r}, nombre={self.nombre!r}, categoria={self.categoria!r})"