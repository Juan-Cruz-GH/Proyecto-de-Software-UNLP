from src.core.db import db
#Tabla N a N de Permiso con Rol
Permiso_Rol=db.Table(
    "Permiso_Rol",
    db.column("id_permiso",db.Integer,db.ForeignKey("Permisos.id"), nullable=False, primary_key=True),
    db.column("id_rol", db.Integer,db.ForeignKey("Roles.id"), nullable=False, primary_key=True),
)

class Permiso(db.model):
    __tablename__ = "Permisos"

    #columnas
    id=db.column(db.Integer, primary_key=True, nullable=False, unique=True)
    nombre= db.column(db.String(100), nullable=False)
    
    #relacion
    roles=db.relationship("Rol", secondary=Permiso_Rol)

