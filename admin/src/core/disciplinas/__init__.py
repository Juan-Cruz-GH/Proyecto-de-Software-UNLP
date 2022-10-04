from src.core.disciplinas.disciplinas import Disciplina

def listar_disciplinas():
    return Disciplina.query.all()