from src.web.controllers.validators.common_validators import (
    is_integer,
    valor_fuera_de_rango_float,
    validar_longitud,
    is_positive_float,
    is_float,
)


def validar_inputs(data):
    if datos_estan_vacios(data):
        return False, "Todos los datos deben llenarse"
    if not is_integer(data["elementos_pagina"]):
        return False, "Elementos por página debe ser un numero"
    if not is_float(data["porcentaje_recargo"]):
        return False, "El porcentaje de recargo no es un flotante"
    if not is_float(data["cuota_base"]):
        return False, "La cuota base no es un flotante"
    if not is_positive_float(data["porcentaje_recargo"]):
        return False, "El porcentaje de recargo no es positivo"
    if not is_positive_float(data["cuota_base"]):
        return False, "La cuota base no es positiva"
    if not validar_longitud(data["informacion_contacto"]):
        return False, "La información de contacto es demasiado larga"
    if not validar_longitud(data["encabezado_recibos"]):
        return False, "El encabezado de los recibos es demasiado largo"
    if valor_fuera_de_rango_float(data["cuota_base"]):
        return False, "La cuota base es demasiado grande"
    return True, "Los datos son validos"


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
