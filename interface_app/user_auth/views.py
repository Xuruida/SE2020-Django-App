from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo

# avoid error 403
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            UserInfo.objects.get(username=username)
            return HttpResponse("Username: %s has already existed." % username)
        except BaseException:
            newUser = UserInfo(username=username, password=password)
            newUser.save()
            return HttpResponse("Created new user %s!\n" % username)
    return HttpResponse("Please use POST method to signup.")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            return HttpResponse("Please input username")
        password = request.POST.get('password')
        if not password:
            return HttpResponse("Please input password")
        try:
            user_info = UserInfo.objects.get(username=username)
            if user_info.password == password:
                return HttpResponse("Password correct. Login succeeded.")
            else:
                return HttpResponse("Password incorrect. Login failed.")
        except BaseException:
            return HttpResponse("User: %s has not register. Please sign up." % username)