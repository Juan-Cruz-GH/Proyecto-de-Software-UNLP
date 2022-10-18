from src.core import usuarios

def check_permission(user, permission):
    return usuarios.has_permission(user, permission)