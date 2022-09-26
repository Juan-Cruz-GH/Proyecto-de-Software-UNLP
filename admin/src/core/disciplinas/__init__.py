from src.core.disciplinas import Disciplina

def listar_disciplinas():
    return Disciplina.query.all()