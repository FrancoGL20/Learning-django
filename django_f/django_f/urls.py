"""
URL configuration for django_f project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cursos.views import cursos,cursosAPI,mostrarFormulario
from django.http import HttpResponse

def funcion(request):
    print(request.headers)
    return HttpResponse('<h1>Hola mundo django</h1>')


def saludo(request):
    nombre=request.GET['nombre']
    return HttpResponse(f'<h1>Hola {nombre} django</h1>')


def suma(request,n1,n2):
    suma=n1+n2
    return HttpResponse(f'<h1>El resultado es {suma}</h1>')


urlpatterns = [
    path('funcion/',funcion),
    path('cursos/api/',cursosAPI),
    path('saludo/',saludo),
    path('suma/<int:n1>/<int:n2>/',suma),
    path('cursos/',cursos),
    path('form/',mostrarFormulario),
    path('admin/', admin.site.urls),
]
