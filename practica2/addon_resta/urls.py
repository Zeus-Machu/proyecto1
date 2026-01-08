from django.urls import path
from . import views

app_name = 'addon_resta'

urlpatterns = [
    path('', views.restar, name='restar'),
]