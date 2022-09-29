from src.core.db import db

class Configuracion_general(db.Model):
    __tablename__="configuracion_general"

    id=db.Column(db.Integer, primary_key=True, nullable= False, unique=True)
    activar_pagos=db.Column(db.Boolean, nullable=False)
    encabezado_recibos=db.Column(db.String(500), nullable=False)
    informacion_contacto=db.Column(db.String(500), nullable=False)
    cuota_base= db.Column(db.Float, nullable=False)
    porcentaje_recargo=db.Column(db.Float, nullable=False)