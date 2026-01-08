from django.urls import path
from . import views

app_name = 'addon_cuadrado'

urlpatterns = [
    path('', views.cuadrado , name='cuadrado'),
]