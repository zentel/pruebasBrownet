from django.conf.urls import url, include
from . import views
from rest_framework import routers

urlpatterns = [
	url(r'^usuarios/$',views.ListUsers.as_view()),
	url(r'^tokens/$', views.token),
]