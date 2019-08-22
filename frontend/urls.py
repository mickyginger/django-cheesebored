from django.urls import path, re_path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.Home.as_view()),
    re_path(r'^(?P<filename>[\w\.]+)$', views.Assets.as_view()),
]
