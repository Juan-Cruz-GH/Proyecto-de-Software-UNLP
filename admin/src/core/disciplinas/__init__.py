from src.core import configuracion_sistema
from src.core.socios import buscar_socio
from src.core.disciplinas.disciplinas import Disciplina
from src.core.db import db


def relacionar_socio_disciplina(idDisciplina, idSocio):
    disciplina = buscar_disciplina(idDisciplina)
    socio = buscar_socio(idSocio)
    disciplina.socios.append(socio)
    db.session.commit()


def estaHabilitada(id):
    return buscar_disciplina(id).habilitada


def listar_disciplinas_diccionario():
    """Devuelve una lista de diccionarios con todas las disciplinas."""
    lista = []
    disciplinas = Disciplina.query.all()
    for disciplina in disciplinas:
        fila = disciplina.__dict__
        dias_horarios = fila["horarios"].split(" de ")
        diccionario = {
            "name": fila["nombre"],
            "days": dias_horarios[0],  # hay que consultar con el ayudante
            "time": dias_horarios[1],  #
            "teacher": fila["instructores"],
        }
        lista.append(diccionario)
    return lista


def todas_las_disciplinas():
    nombres = db.session.query(Disciplina.nombre.distinct()).all()
    return nombres


def categorias_de_cada_disciplina():
    disciplinas = todas_las_disciplinas()
    todas_las_categorias = {}
    for disciplina in disciplinas:
        categorias = (
            db.session.query(Disciplina.categoria, Disciplina.id)
            .filter(Disciplina.nombre == disciplina[0])
            .all()
        )
        for categoria in categorias:
            todas_las_categorias[disciplina[0]] = categorias
    return todas_las_categorias


def listar_disciplinas(page):
    """Listado de las disciplinas según el paginado definido en el módulo de configuración"""
    return Disciplina.query.paginate(
        page, per_page=configuracion_sistema.get_paginado().elementos_pagina
    )


def buscar_disciplina(id):
    """Devuelve la disciplina con el id indicado"""
    return Disciplina.query.get(id)


def agregar_disciplina(data):
    """Dar de alta una disciplina en la BD"""
    disciplina = Disciplina(**data)
    db.session.add(disciplina)
    db.session.commit()
    return disciplina


def eliminar_disciplina(id):
    """Dar de baja una disciplina en la BD buscandola por su id que seguro existe"""
    db.session.delete(Disciplina.query.get(id))
    db.session.commit()


def modificar_disciplina(data):
    """Modificar datos de una disciplina en la BD"""
    disciplina = Disciplina.query.get(data["id"])
    disciplina.nombre = data["nombre"]
    disciplina.categoria = data["categoria"]
    disciplina.instructores = data["instructores"]
    disciplina.horarios = data["horarios"]
    disciplina.costo = data["costo"]
    disciplina.habilitada = data["habilitada"]
    db.session.commit()
    return disciplina


def validar_disciplina_repetida(nombre, categoria, accion, id=None):
    """Chequea que no haya ya una disciplina con mismo nombre y misma categoria"""
    if accion == "alta":
        nombre_existente = (
            Disciplina.query.filter_by(nombre=nombre)
            .filter(Disciplina.categoria == categoria)
            .first()
        )
        if nombre_existente is None:
            return True, "La disciplina no existe aún"
        else:
            return False, "La disciplina ya existe"
    elif accion == "modificacion":
        nombre_existente = (
            Disciplina.query.filter_by(nombre=nombre)
            .filter(Disciplina.categoria == categoria)
            .filter(Disciplina.id != id)
            .first()
        )
        if nombre_existente is None:
            return True, "La disciplina no existe aún"
        else:
            return False, "La disciplina ya existe"
