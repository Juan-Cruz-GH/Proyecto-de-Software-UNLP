from src.core.socios.socios import Socio

def listar_socios():
    return Socio.query.all()