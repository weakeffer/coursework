from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.register_user, name = 'register_user'),
    path('login/', views.login_user, name = 'login_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),

]