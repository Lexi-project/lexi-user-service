from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('health-check', views.check_health, name='register'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='get-access-and-refresh-token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='refresh-token'),
]
