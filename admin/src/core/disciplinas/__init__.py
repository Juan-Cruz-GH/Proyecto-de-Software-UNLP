from src.core.disciplinas.disciplinas import Disciplina
from src.core.db import db

def listar_disciplinas(page):
    '''Listado de las disciplinas según el paginado definido en el módulo de configuración.'''
    return Disciplina.query.paginate(page, per_page=5)  # hardcodeado a 5 por ahora, luego consultará al modulo de cfg

def agregar_disciplina(data):
    '''Dar de alta una disciplina en la BD, chequeando que no exista primero.'''
    if( Disciplina.query.filter_by(nombre = data["nombre"]).first() ):
        return "Ya existe la disciplina."
    else:
        disciplina = Disciplina(**data)
        db.session.add(disciplina)
        db.session.commit()
        return disciplina

def eliminar_disciplina(id):
    '''Dar de baja una disciplina en la BD.'''
    disciplina = Disciplina.query.get(id)
    if(disciplina is not None):
        db.session.delete(disciplina)
        db.session.commit()

def modificar_disciplina(data):
    '''Modificar datos de una disciplina en la BD.'''
    disciplina = Disciplina.query.get(data["id"])
    disciplina.nombre = data["nombre"]
    disciplina.categoria = data["categoria"]
    disciplina.instructores = data["instructores"]
    disciplina.horarios = data["horarios"]
    disciplina.costo = data["costo"]
    disciplina.habilitada = data["habilitada"]
    db.session.commit()
    return disciplina
