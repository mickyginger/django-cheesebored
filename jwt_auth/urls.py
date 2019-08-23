from django.urls import path

from . import views

app_name = 'jwt_auth'
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
]
