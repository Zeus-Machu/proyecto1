from django.urls import path
from .views import calcular
app_name = 'addon_polinomios'

urlpatterns = [
    path('', calcular, name='calcular'),
]
  
