from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer

# Create your views here.
def index(request):
	lista_usuarios = Usuario.objects.order_by('apellido')[:10]
	output = ', '.join([p.nombre for p in lista_usuarios])

	return HttpResponse(output)

class UsuarioViewSet(viewsets.ModelViewSet):
	#	API endpoint
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer