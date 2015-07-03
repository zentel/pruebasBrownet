from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from rest_framework import authentication,permissions

# Create your views here.
def index(request):
	lista_usuarios = Usuario.objects.order_by('apellido')[:10]
	output = ', '.join([p.nombre for p in lista_usuarios])

	return HttpResponse(output)

#creación de tokens
def token(request):
	#TODO: cambiar a POST
	username = request.GET['user']
	password = request.GET['password']
	usuario = authenticate(username=username,password=password)
	if usuario is not None:
		if usuario.is_active:
			tok = Token.objects.get(user=usuario)

			#Si el token no existe lo creo
			if tok is None:
				tok = Token.objects.create(user=usuario)

			return HttpResponse("Token: " + tok.key)
		else:
			return HttpResponse("Usuario no activo")
	else:
		return HttpResponse('Usuario invalido')

class ListUsers(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)


	def get(self, request, format=None):
		#	API endpoint
		queryset = Usuario.objects.all()
		serializer = UsuarioSerializer(queryset, many=True)
		return Response(serializer.data)