from django.urls import path
from . import views

app_name = 'addon_factorizacion'

urlpatterns = [
    path('', views.factorizacion, name='factorizacion'),
]
