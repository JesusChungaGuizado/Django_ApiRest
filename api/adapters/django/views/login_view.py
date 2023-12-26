from django.contrib.auth.hashers import check_password
from django.core.serializers import serialize

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ....core.entities.users import User
import requests
import json

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password') 
        ip_cliente = self.obtener_ip_cliente()
        print(ip_cliente)
        try:
            usuario = User.objects.get(email=email)                                     #buscando el emaiL
            usuario_json=json.loads(serialize('json',[usuario]))[0]['fields'] 
            if check_password(password, usuario.password) :                             #verificando el hash encriptado del email ingresado
                refresh = RefreshToken()                                                #Generando Token
                refresh['user_json'] = usuario_json                                     #pasando info de usuario al token
                access_token = str(refresh.access_token)                                #capturando el token generado
                return Response({'user':usuario_json,'token': access_token}, status=200)
            else:
                return Response({'message': 'Contraseña Invalida'}, status=404)
            
        except User.DoesNotExist:
            return Response({"message": "No existe el email ingresado"}, status=404)
    
    def obtener_ip_cliente(self):

        
        # Verificar si la dirección IP está presente en las cabeceras HTTP
        # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        # if x_forwarded_for:
        #     # La dirección IP está en la cadena X-Forwarded-For
        #     ip_cliente = x_forwarded_for.split(',')[0].strip()
        # else:
        #     # Utilizar la dirección IP directa del cliente
        #     ip_cliente = request.META.get('REMOTE_ADDR')

        # return ip_cliente

        # SERVICIO EXTERNO
        try:
            # Utilizar un servicio externo para obtener la dirección IP pública
            response = requests.get('https://api64.ipify.org?format=json')
            ip_data = response.json()
            ip_cliente = ip_data.get('ip')
            return ip_cliente
        except Exception as e:
            # Manejar cualquier error al obtener la dirección IP pública
            return f"Error: {str(e)}"