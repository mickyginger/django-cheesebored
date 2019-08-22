from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('cheeses.urls')),
    re_path(r'^(?P<filename>[\w\.]+)$', views.Assets.as_view()),
    path('', views.Home.as_view())
]
