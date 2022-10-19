from src.core import usuarios

def check_permission(user, permission):
    """Manda a validar al modelo si un usuario tiene los permisos necesarios para ingresar a una vista"""
    return usuarios.has_permission(user, permission)