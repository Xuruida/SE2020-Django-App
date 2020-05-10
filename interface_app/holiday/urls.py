from django.urls import path
from . import views

urlpatterns = [
    path('festival', views.holiday, name='holiday')
]