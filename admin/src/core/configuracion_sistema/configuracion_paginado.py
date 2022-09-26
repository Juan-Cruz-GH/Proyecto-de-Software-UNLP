from src.core.db import db

class configuracion_sistema(db.model):
    __tablename__="configutacion_paginado"

    id=db.column(db.Integer, primary_key=True, nullable= False, unique=True)
    elementos_pagina=db.column(db.Integer, nullable=False)
    