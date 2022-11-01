# Cosas que faltan arreglar a la fecha 29 octubre:
* Dividir exportaciones en 2 archivos y ponerlos dentro de un directorio
* Lineas de código deben tener length 79 como máximo
* Ocultar el botón "Configuración" si el usuario logueado es Operador
* [La búsqueda de usuarios por email no debería ser estricta, si no que debería mostrar los usuarios cuyo email **contiene** esa query](https://docs.sqlalchemy.org/en/14/core/sqlelement.html#sqlalchemy.sql.expression.ColumnOperators.contains)
* No se debe poder crear un usuario sin roles
* El botón de desactivar admin debe estar bloqueado o invisible
* Módulo pagos tira error 502 cuando el ayudante creó un usuario nuevo y quiso pagarle una cuota