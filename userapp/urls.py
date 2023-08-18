from django.urls import path
from . import views

urlpatterns = [
    path('health-check', views.check_health, name='register'),
]
