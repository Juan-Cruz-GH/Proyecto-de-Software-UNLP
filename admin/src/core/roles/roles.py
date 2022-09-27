from src.core.db import db

#Tabla N a N de Usuario con Rol
Usuario_Rol=db.Table(
    "Permiso_Rol",
    db.column("id_usuario",db.Integer,db.ForeignKey("Usuario.id"), nullable=False, primary_key=True),
    db.column("id_rol", db.Integer,db.ForeignKey("Roles.id"), nullable=False, primary_key=True),
)

class Rol(db.model):
    __tablename__="Roles"

    #Columnas
    id=db.column(db.Integer, primary_key=True, nullable=False, unique=True)
    nombre= db.column(db.String(100), nullable=False)

    #Relacion
    usuarios=db.relationship("Usuario", secondary=Usuario_Rol)