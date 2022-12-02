def validar_inputs(json):
    # El json en sí siempre va a ser enviado, por cómo está definido
    # el frontend y por tener el jwt_required en la api.
    if datos_estan_vacios(json):
        return False  # El mes y el monto deben estar presentes
    if not es_numero(json["month"]):
        return False  # El mes no es un número
    if not es_numero(json["amount"]):
        return False  # El monto no es un número
    if not es_mes(json["month"]):
        return False  # El mes no es un mes
    return True  # Datos válidos


def datos_estan_vacios(json):
    """Si alguno de los datos está vacio retorna verdadero"""
    if json["month"] == "" or json["amount"] == "":
        return True


def es_numero(dato):
    return dato.lstrip("-").isdigit()


def es_mes(mes):
    return mes in range(1, 13)