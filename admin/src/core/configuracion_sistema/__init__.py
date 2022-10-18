from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from src.core.configuracion_sistema.configuracion_general import Configuracion_general
from src.core.db import db


def getPaginado():
    """Devuelve la tupla que contiene el campo "elementos_pagina" que se usa para determinar cuantos elementos se muestran por pagina"""
    return Configuracion_paginado.query.first()


def getConfiguracionGeneral():
    "Devuelve la tupla de configuracion general que contiene los campos: activar_pagos, encabezado_recibos,informacion_contacto, cuota_base y porcentaje_recargo"
    return Configuracion_general.query.first()


def configuracionPredeterminada():
    """Crea una configuracion predeterminada para la configuracion del sistema"""
    paginado = Configuracion_paginado(10)
    configuracion = Configuracion_general(
        False, "Encabezado para los recibos", "Informacion de Conctacto del club", 0, 0
    )
    db.session.add(paginado)
    db.session.add(configuracion)
    db.session.commit()
    return paginado, configuracion


def modificar_configuracion(data, data_paginado):
    """Actualiza los datos de configuracion del sistema"""
    # Recuperar cantidad de paginas, si no existe la fila en la db se la crea
    paginado = Configuracion_paginado.query.first()
    if paginado == None:
        paginado = Configuracion_paginado(**data_paginado)
        db.session.add(paginado)
    else:
        paginado.elementos_pagina = data_paginado["elementos_pagina"]

    # Recuperar configuracion general, si no existe la fila en la db se la crea
    configuracion = Configuracion_general.query.first()
    if configuracion == None:
        configuracion = Configuracion_general(**data)
        db.session.add(configuracion)
    else:
        configuracion.activar_pagos = data["activar_pagos"]
        configuracion.encabezado_recibos = data["encabezado_recibos"]
        configuracion.informacion_contacto = data["informacion_contacto"]
        configuracion.cuota_base = data["cuota_base"]
        configuracion.porcentaje_recargo = data["porcentaje_recargo"]

    db.session.commit()
    return paginado


def validar_digito(dato):
    """Valida que un dato sea un flotante. El return devuelve dos objetos: booleano, mensaje"""
    try:
        n = float(dato)
    except ValueError:
        return False, "no es un dígito valido"
    return True, "Dígito valido"


def validad_entero(dato):
    """Valida que un dato sea un entero. El return devuelve dos objetos: booleano, mensaje"""
    try:
        n = int(dato)
    except ValueError:
        return False, "Ingrese un número valido"
    return True, "Número valido"


def validar_positivo(dato):
    return float(dato) >= 0, "debe ser un número positivo"


def validar_cadena(dato):
    if len(dato) > 500:
        return False, "Límite de caracteres excedido"
    return True, "Cadena valida"
