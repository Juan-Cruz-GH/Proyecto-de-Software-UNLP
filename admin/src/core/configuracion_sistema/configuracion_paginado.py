from src.core.db import db

class Configuracion_paginado(db.model):
    __tablename__="configuracion_paginado"

    id=db.column(db.Integer, primary_key=True, nullable= False, unique=True)
    elementos_pagina=db.column(db.Integer, nullable=False)

    def __init__(self, elementos_pagina=none):
        self.elementos_pagina=elementos_pagina

    