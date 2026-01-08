from django.urls import path
from . import views

app_name = 'addon_rectangulo'

urlpatterns = [
    path('', views.rectangulo , name='rectangulo'),
]