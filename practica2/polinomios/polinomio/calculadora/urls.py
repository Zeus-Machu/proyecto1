from django.urls import path
from .views import calcular_polinomios

urlpatterns = [
    path('', calcular_polinomios, name='calculadora'),
]
  