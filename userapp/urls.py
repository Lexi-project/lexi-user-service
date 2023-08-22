from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

urlpatterns = [
    path('health-check', views.check_health, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login-user'),
]
