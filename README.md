# Grupo 23

Juan Cruz Cassera Botta 17072/7

Nicolas Pierini 12707/7

Manuel Trotta 17395/4

Leiva Hernán Adrián 15495/8

# Base de datos
Filas que agregar a las tablas:
Tabla "Usuarios:

Al menos un usario cuya contraseña se debe almacenar con el siguiente hash que es para la contraseña "admin123":
sha256$3avTC9Ehs6jgGDl6$de25a296fd1ba76933c0c994eb0fb617b78b9352339927cc09504ec6341ce758


Tabla "Permisos":
Agregar los siguientes permiso siguiendo la sintaxis modulo_accion(ejemplos: usuario_index, disciplina_new):

usuario: index, new, update, destroy
disciplina: index, new, update, destroy
socio: index, new, update, destroy
pago: index, pay, download
configuracion: index, update


Tabla "Roles":
Rol que represente a un administrador, ejemplo: "rol_administrador"
Rol que represente a un operador: "rol operador"


Tabla "Permiso_Rol":
Crear tuplas que relacionen a los roles de la siguiente forma:

Rol de operador: 
-Para socio, disciplina, permisos de: index, new, update
-Para usuario, permisos de: index
-para pago: index, pay, download

Rol de administrador: 
-Todos los permisos de operador
-Ademas para socio y disciplina permisos de: destroy
-Para usuario: new, update, destroy
-Para configuracion: index, update


Tabla "Usuario_Rol"