from django.urls import path
from . import views

app_name = 'addon_circulo'

urlpatterns = [
    path('', views.circulo , name='circulo'),
]