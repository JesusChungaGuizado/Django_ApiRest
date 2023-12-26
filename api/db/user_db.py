from django.db import connection
from django.http import JsonResponse
from ..core.entities.users import User
def listar_usuario():
    with connection.cursor() as cursor:
        cursor.callproc('ListUser')
        result = cursor.fetchall()  
        # Obtener resultados si hay
        column_names = [col[0] for col in cursor.description]
        # Convertir el resultado a una lista de diccionarios con nombres de columna
        data = [dict(zip(column_names, row)) for row in result]
        return data

def showUser(id:int):
    with connection.cursor() as cursor:
        cursor.callproc('showUser',[id])
        result = cursor.fetchall() 
        if result:
            row = result[0]
            column_names = [col[0] for col in cursor.description]
            data = dict(zip(column_names, row))
            return data
        else:
            return None

def updateUser(user:User):
    with connection.cursor() as cursor:
        try:
            # Ejecutar el procedimiento almacenado
            cursor.callproc('updateUser',[user.id,user.name,user.last_name])
            # Confirmar los cambios
            connection.commit()
            return True;
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante la ejecución del procedimiento almacenado
            connection.rollback()
            return {"error": str(e)}
  
        


def loginUser(email,password):
    with connection.cursor() as cursor:
        cursor.callproc('inicioSesion',[email,password])
        result = cursor.fetchall() 
        if result:
            row = result[0]
            column_names = [col[0] for col in cursor.description]
            data = dict(zip(column_names, row))
            return data
        else:
            return None