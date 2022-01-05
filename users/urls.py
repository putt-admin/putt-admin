from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setup', views.setup, name='setup'),
    path('builder', views.builder, name='builder'),
]
