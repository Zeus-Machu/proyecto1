from django.urls import path
from . import views

app_name = "addon_primera"

urlpatterns = [
    path("", views.ecuacion_primera, name="ecuacion"),
]
