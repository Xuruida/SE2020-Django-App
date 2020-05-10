from django.urls import path
from . import views

urlpatterns = [
    path('holiday', views.holiday, name='holiday')
]