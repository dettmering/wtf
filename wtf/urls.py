from django.contrib import admin
from django.urls import path, include

from . import views, api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index),
    path('add/', views.add_wtf),
    path('api/today', api.today),
]
