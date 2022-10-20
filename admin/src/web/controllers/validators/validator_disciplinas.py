import re


def validar_inputs(data):
    """Chequea que los datos del formulario sean válidos"""
    if (
        data["nombre"] == ""
        or data["categoria"] == ""
        or data["instructores"] == ""
        or data["horarios"] == ""
        or data["costo"] == ""
        or data["habilitada"] == ""
    ):
        return False, "Todos los datos deben llenarse"
    elif not data["costo"].lstrip("-").isdigit():
        return False, "El costo debe ser un numero"
    elif int(data["costo"]) < 0:
        return False, "El costo no puede ser negativo"
    elif not (re.fullmatch(r"[A-Za-z ]{1,50}", data["nombre"])):
        return False, "El nombre de la disciplina no puede tener numeros"
    elif "de" not in data["horarios"]:
        return (
            False,
            'El formato de los horarios es incorrecto, debe ser "Dia1 Dia2 (opcional) de X a Yhs"',
        )
    else:
        return True, "Los datos son validos"
