from django.urls import path
from . import views

app_name = 'addon_recta'

urlpatterns = [
    path('', views.recta, name='recta'),
]