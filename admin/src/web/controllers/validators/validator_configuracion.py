from src.web.controllers.validators.common_validators import es_entero


def validar_inputs(data):
    if datos_estan_vacios(data):
        return False, "Todos los datos deben llenarse"
    if not es_entero(data["elementos_pagina"]):
        return False, "Elementos por página debe ser un numero"
    if not validar_flotante(data["porcentaje_recargo"]):
        return False, "El porcentaje de recargo no es un flotante"
    if not validar_flotante(data["cuota_base"]):
        return False, "La cuota base no es un flotante"
    if not validar_positivo(data["porcentaje_recargo"]):
        return False, "El porcentaje de recargo no es positivo"
    if not validar_positivo(data["cuota_base"]):
        return False, "La cuota base no es positiva"
    if not validar_longitud(data["informacion_contacto"]):
        return False, "La información de contacto es demasiado larga"
    if not validar_longitud(data["encabezado_recibos"]):
        return False, "El encabezado de los recibos es demasiado largo"
    if valor_fuera_de_rango(data["cuota_base"]):
        return False, "La cuota base es demasiado grande"


def datos_estan_vacios(data):
    """Si alguno de los datos está vacio retorna verdadero"""
    if (
        data["elementos_pagina"] == ""
        or data["encabezado_recibos"] == ""
        or data["informacion_contacto"] == ""
        or data["cuota_base"] == ""
        or data["porcentaje_recargo"] == ""
    ):
        return True


def validar_flotante(dato):
    """Valida que un dato sea un flotante. El return devuelve dos objetos: booleano, mensaje"""
    try:
        float(dato)
    except ValueError:
        return False
    return True


def validar_positivo(dato):
    return float(dato) >= 0


def validar_longitud(dato):
    return len(dato) <= 500


def valor_fuera_de_rango(dato):
    return float(dato) > 1_000_000
