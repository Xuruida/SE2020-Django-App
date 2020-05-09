from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

# avoid error 403
from django.views.decorators.csrf import csrf_exempt

# import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            return HttpResponse("Username: %s has already existed." % username)
        except:
            User.objects.create_user(username, password=password)
            return HttpResponse("Created new user: %s!\n" % username)
    return HttpResponse("Please use POST method to signup.")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            return HttpResponse("Please post username")
        password = request.POST.get('password')
        if not password:
            return HttpResponse("Please post password")

        user = authenticate(username=username, password=password)
        if user is not None:
            return HttpResponse("Password correct. Login succeeded.")
        else:
            return HttpResponse("username or password is not correct")
