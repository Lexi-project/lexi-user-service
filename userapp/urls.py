from django.urls import path
from . import views

urlpatterns = [
    path('health-check', views.check_health, name='register'),
    path('login/', views.UserLoginAPIView.as_view(),
         name='login-user'),
]
