from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from src.core.db import db

class Pago(db.Model):
    __tablename__ = "Pagos"
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Integer, nullable=False)
    fecha_pago = db.Column(db.DateTime, nullable=False)
    socio_id = db.Column(db.Integer, db.ForeignKey("Socios.id"))
    socio = db.relationship("Socio", back_populates="pagos")

    def __init__(self, total=None, fecha_pago=None, socio_id=None):
        self.total = total
        self.fecha_pago = fecha_pago
        self.socio_id = socio_id

    def __repr__(self):
        return f"Socio(id={self.id!r}, total={self.total!r}, fecha={self.fecha_pago!r})"