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