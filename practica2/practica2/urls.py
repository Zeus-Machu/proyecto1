"""
URL configuration for practica2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),              
    path('suma/', include('addon_suma.urls')),  
    path('resta/', include('addon_resta.urls')),
    path('div/', include ('addon_div.urls')),
    path('multi/', include ('addon_multi.urls')),
    path('circulo/', include ('addon_circulo.urls')),
    path('cuadrado/', include ('addon_cuadrado.urls')),
    path('rectangulo/', include ('addon_rectangulo.urls')),
    path('ecuacion',include('addon_ecuacion.urls')),
    path('recta',include('addon_recta.urls')),
    path('admin/', admin.site.urls),
]