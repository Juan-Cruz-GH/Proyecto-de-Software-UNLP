import re
from src.core import configuracion_sistema
from src.core.disciplinas.disciplinas import Disciplina
from src.core.db import db

def listar_disciplinas_diccionario():
    '''Devuelve una lista de diccionarios con todas las disciplinas.'''
    lista = []
    disciplinas = Disciplina.query.all()
    for disciplina in disciplinas:
        row = disciplina.__dict__
        row.pop("_sa_instance_state")
        row.pop("inserted_at")
        lista.append(row)
    return lista
    
def listar_disciplinas(page):
    '''Listado de las disciplinas según el paginado definido en el módulo de configuración'''
    return Disciplina.query.paginate(page, per_page=configuracion_sistema.getPaginado().elementos_pagina)  

def buscar_disciplina(id):
    '''Devuelve la disciplina con el id indicado'''
    return Disciplina.query.get(id)

def agregar_disciplina(data):
    '''Dar de alta una disciplina en la BD'''
    disciplina = Disciplina(**data)
    db.session.add(disciplina)
    db.session.commit()
    return disciplina

def eliminar_disciplina(id):
    '''Dar de baja una disciplina en la BD buscandola por su id que seguro existe'''
    db.session.delete(Disciplina.query.get(id))
    db.session.commit()

def modificar_disciplina(data):
    '''Modificar datos de una disciplina en la BD'''
    disciplina = Disciplina.query.get(data["id"])
    disciplina.nombre = data["nombre"]
    disciplina.categoria = data["categoria"]
    disciplina.instructores = data["instructores"]
    disciplina.horarios = data["horarios"]
    disciplina.costo = data["costo"]
    disciplina.habilitada = data["habilitada"]
    db.session.commit()
    return disciplina

def validar_disciplina_repetida(nombre, accion, id=None):
    '''Chequea que la disciplina no exista ya'''
    if(accion == "alta"):
        nombre_existente = Disciplina.query.filter_by(nombre=nombre).first()
        if(nombre_existente is None):
            return True, "La disciplina no existe aún"
        else:
            return False, "La disciplina ya existe"
    elif(accion == "modificacion"):
        nombre_existente = Disciplina.query.filter_by(nombre=nombre).filter(Disciplina.id != id).first()
        if(nombre_existente is None):
            return True, "La disciplina no existe aún"
        else:
            return False, "La disciplina ya existe"

def validar_inputs(data):
    '''Chequea que los datos del formulario sean válidos'''
    if(data["nombre"] == '' or data["categoria"] == '' or data["instructores"] == '' or data["horarios"] == '' or data["costo"] == '' or data["habilitada"] == ''):
        return False, "Todos los datos deben llenarse"
    elif(not data["costo"].lstrip("-").isdigit()):
        return False, "El costo debe ser un numero"
    elif(int(data["costo"]) < 0):
        return False, "El costo no puede ser negativo"
    elif not(re.fullmatch(r"[A-Za-z ]{1,50}", data["nombre"])):
        return False, "El nombre de la disciplina no puede tener numeros"
    else:
        return True, "Los datos son validos"
