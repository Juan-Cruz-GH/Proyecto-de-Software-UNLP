from flask import Blueprint, render_template
from src.core import disciplinas

disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

@disciplina_blueprint.get("/")
def disciplinas_index():
    kwargs = {"disciplinas" : disciplinas.listar_disciplinas()}
    return render_template("disciplinas/disciplinas.html", **kwargs)