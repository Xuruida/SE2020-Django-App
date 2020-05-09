from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

# Create your views here.

def signup(request):
    return HttpResponse("Hello world.")