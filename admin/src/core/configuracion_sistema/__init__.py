from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from src.core.configuracion_sistema.configuracion_general import Configuracion_general
from src.core.db import db

def getPaginado():
    return Configuracion_paginado.query.first()

def getConfiguracionGeneral():
    return Configuracion_general.query.first()

def modificar_configuracion(data, data_paginado):
    paginado = Configuracion_paginado.query.first()
    paginado.elementos_pagina=data_paginado["elementos_pagina"]
    config= Configuracion_general.query.first()
    if (config ==None):
        config= Configuracion_general(**data)
        db.session.add(config)
    else:
        config.activar_pagos= data["activar_pagos"]
        config.encabezado_recibos= data["encabezado_recibos"]
        config.informacion_contacto=data["informacion_contacto"]
        config.cuota_base=data["cuota_base"]
        config.porcentaje_recargo=data["porcentaje_recargo"]
    db.session.commit()
    return paginado

    