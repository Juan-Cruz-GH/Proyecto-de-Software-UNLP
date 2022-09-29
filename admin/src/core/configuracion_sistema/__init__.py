from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from src.core.configuracion_sistema.configuracion_general import Configuracion_general
def getPaginado():
    return Configuracion_paginado.query.all()

def getConfiguracionGeneral():
    return Configuracion_general.query.all()
    