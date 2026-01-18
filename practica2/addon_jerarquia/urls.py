from django.urls import path
from . import views
app_name = 'addon_jerarquia'

urlpatterns = [
    path('jerarquia/', views.jerarquia_operaciones, name='jerarquia'),
]
