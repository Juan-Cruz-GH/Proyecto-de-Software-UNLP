from src.core.configuracion_sistema.configuracion_paginado import Configuracion_paginado
from src.core.configuracion_sistema.configuracion_general import Configuracion_general
from src.core.db import db


def get_paginado():
    return Configuracion_paginado.query.first()


def get_configuracion_general():
    return Configuracion_general.query.first()


def get_info_contacto_diccionario():
    """Devuelve un diccionario con la informacion de contacto"""
    info = (get_configuracion_general().informacion_contacto).split(" | ")
    email = info[0]
    telefono = info[1]
    diccionario = {"email": email, "phone": telefono}
    return diccionario


def configuracion_predeterminada():
    paginado = Configuracion_paginado(10)
    configuracion = Configuracion_general(
        False, "Encabezado para los recibos", "Informacion de Conctacto del club", 0, 0
    )
    db.session.add(paginado)
    db.session.add(configuracion)
    db.session.commit()
    return paginado, configuracion


def modificar_configuracion(data, data_paginado):
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
