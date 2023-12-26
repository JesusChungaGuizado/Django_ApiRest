
from django.utils import timezone
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets
from rest_framework.response import Response

from ....core.entities.users import User
from ....core.use_cases.user_user_case import listUser,showUser
from ....core.use_cases.validate_token import validateToken

import json

class UserViewSet(viewsets.ViewSet):
    # Metodo para listar usuarios
    def list(self,request):
        validation=validateToken(request)
        if validation:
            result = listUser()
            return Response({"data":result},status=200)
        else:
            return Response({"message":"No tiene autorización 401"},status=401)
        
    #Metodo para buscar usuario x id
    def show(self,request,id):
        validation=validateToken(request)
        if validation:
            try:
                usuario=User.objects.get(id=id)
                datos_usuario = json.loads(serialize('json',[usuario]))[0]['fields']
                
                return Response(datos_usuario,status=200)
            except User.DoesNotExist:
                return Response({"message":"El usuario con el ID especificado no existe"},status=404)
        else:
            return Response({"message":"No tiene autorización 401"},status=401)

    # Crear nuevo usuario
    def create(self,request):
        validation=validateToken(request)
        if validation:
            try:
                response=request.data
                if User.objects.filter(email=response['email']).exists():
                    print(timezone.localtime(timezone.now()))
                    return Response({"message": "El correo electrónico ya está en uso"}, status=400)
                else:
                    usuario=User(
                        name=response['name'],
                        last_name=response['last_name'],
                        email=response['email'],
                        password=make_password(response['password']),
                        created_at= timezone.localtime(timezone.now())
                    )
                   
                    print(timezone.localtime(timezone.now()))
                    usuario.save()
                    return Response({"message": "Usuario Creado"})
            except Exception as e:
                return {"error": str(e)}
        else:
            return Response({"message":"No tiene autorización 401"},status=401)
        
   
    # Actulizar usuario   
    def update(self,request,id):
        validation=validateToken(request)
        if validation:
            try:
                response=request.data
                usuario = User.objects.get(id=id) 
                usuario.name=response['name']
                usuario.last_name=response['last_name']
                usuario.updated_at=timezone.now();
                usuario.save()
                return Response({"message": "Usuario actualizado correctamente"})
            except User.DoesNotExist:
                return Response({"error": "El usuario con el ID especificado no existe"},status=404)
            except Exception as e:
                return {"error": str(e)}
        else:
            return Response({"message":"No tiene autorización 401"},status=401)
        
    
    # Eliminar Usuario
    def destroy(self,request,id):
        validation=validateToken(request)
        if validation:
            try:
                usuario=User.objects.get(id=id)
                usuario.delete()
                return Response({"message":"Usuario eliminado con exito"},status=200)
            except User.DoesNotExist:
                return Response({"message":"El usuario con el ID especificado no existe"},status=404) 
        else:
            return Response({"message":"No tiene autorización 401"},status=401)
       
            

     
        
       

   
