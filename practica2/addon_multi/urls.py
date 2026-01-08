from django.urls import path
from . import views

app_name = 'addon_multi'

urlpatterns = [
    path('', views.multiplicacion, name='multiplicacion'),
]