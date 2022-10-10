from curses.ascii import isdigit
from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from src.core.configuracion_sistema.configuracion_general import Configuracion_general
from src.core.db import db

def getPaginado():
    return Configuracion_paginado.query.first()

def getConfiguracionGeneral():
    return Configuracion_general.query.first()

def modificar_configuracion(data, data_paginado):
    #Recuperar cantidad de paginas, si no existe la fila en la db se la crea
    paginado = Configuracion_paginado.query.first()
    if (paginado == None):
        paginado= Configuracion_paginado(**data_paginado)
        db.session.add(paginado)
    else:
        paginado.elementos_pagina=data_paginado["elementos_pagina"]
    
    #Recuperar configuracion general, si no existe la fila en la db se la crea
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

def validar_digito(dato):
    try:
        n=float(dato)  
    except ValueError:
        return False, "no es un digito valido"
    return True, "Digito valido"
    
def validad_entero(dato):
    try:
        n=int(dato)
    except ValueError:
        return False, "Ingrese numero valido"

def validar_cadena(dato):
    if (len(dato)>500):
        return False, "Limite de caracteres excedido"
    return True, "Cadena valida"
        
    
    