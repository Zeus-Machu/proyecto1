from django.urls import path
from . import views

app_name = 'addon_ecuacion'

urlpatterns = [
    path('', views.ecuacion, name='ecuacion'),
]