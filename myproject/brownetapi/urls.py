from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^', include(router.urls)),
]