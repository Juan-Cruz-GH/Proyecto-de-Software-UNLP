from src.core.disciplinas.disciplinas import Disciplina

def listar_disciplinas(page):
    return Disciplina.query.paginate(page, per_page=1)  # hardcodeado a 1 por ahora, luego consultará al modulo de cfg

