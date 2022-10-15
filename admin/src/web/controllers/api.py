from flask import Blueprint
from src.web.controllers import disciplinas

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/club/disciplinas")
def obtener_disciplinas():
    '''Obtiene el json con todas las disciplinas y lo retorna'''
    return disciplinas.disciplina_json()