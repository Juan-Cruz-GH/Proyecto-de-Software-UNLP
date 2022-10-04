from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado

def getPaginado():
    return Configuracion_paginado.query.all()