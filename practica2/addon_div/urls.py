from django.urls import path
from . import views

app_name = 'addon_div'

urlpatterns = [
    path('', views.divicion, name='divicion'),
]