def is_none(data):
    return data is None


def is_integer(dato):
    return dato.lstrip("-").isdigit()


def is_float(dato):
    """Valida que un dato sea un flotante. El return devuelve dos objetos: booleano, mensaje"""
    try:
        float(dato)
    except ValueError:
        return False
    return True


def is_positive_float(dato):
    return float(dato) >= 0


def validar_longitud(dato, lenght=500):
    return len(dato) <= lenght


def valor_fuera_de_rango_float(dato, max_value=1_000_000):
    return float(dato) > max_value


def valor_fuera_de_rango_entero(dato, valor=1_000_000):
    return int(dato) > valor


def valor_es_negativo_entero(costo):
    return int(costo) < 0
