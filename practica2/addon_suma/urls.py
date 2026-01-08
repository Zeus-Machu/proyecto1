from django.urls import path
from . import views
app_name = 'addon_suma'

urlpatterns = [
    path('', views.sumar, name='sumar'),
]