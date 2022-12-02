import re

from src.web.controllers.validators.common_validators import (
    is_none,
    is_integer,
    valor_fuera_de_rango_entero,
    valor_es_negativo_entero,
)


def validar_inputs(data):
    """Chequea que los datos del formulario sean válidos"""
    if is_none(data["nombre"]):
        return False, "El campo nombre no puede ser nulo"
    if is_none(data["categoria"]):
        return False, "El campo categoría no puede ser nulo"
    if datos_estan_vacios(data):
        return False, "Todos los datos deben llenarse"
    if not is_integer(data["costo"]):
        return False, "El costo debe ser un numero"
    if valor_es_negativo_entero(data["costo"]):
        return False, "El costo no puede ser negativo"
    if valor_fuera_de_rango_entero(data["costo"]):
        return False, "El costo no puede superar un millon(1000000)"
    if not nombre_es_valido(data["nombre"]):
        return False, "El nombre de la disciplina no puede tener numeros"
    if not horario_es_valido(data["horarios"]):
        return (
            False,
            'El formato de los horarios es incorrecto, debe ser "Dia1 Dia2 (opcional) de X a Yhs"',
        )
    return True, "Los datos son validos"


def datos_estan_vacios(data):
    """Si alguno de los datos está vacio retorna verdadero"""
    if (
        data["nombre"] == ""
        or data["categoria"] == ""
        or data["instructores"] == ""
        or data["horarios"] == ""
        or data["costo"] == ""
        or data["habilitada"] == ""
    ):
        return True


def nombre_es_valido(nombre):
    return re.fullmatch(r"[A-Za-z ]{1,50}", nombre)


def horario_es_valido(horarios):
    return "de" in horarios
