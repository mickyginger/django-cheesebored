from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('cheeses', views.CheeseList.as_view(), name='index'),
    path('cheeses/<int:pk>', views.CheeseDetail.as_view(), name='show'),
    path('users', views.UserList.as_view(), name='index'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='show'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
]
