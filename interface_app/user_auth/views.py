from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
# avoid error 403
from django.views.decorators.csrf import csrf_exempt

# import auth
from django.contrib.auth import authenticate

# import token
from rest_framework.authtoken.models import Token

# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        if not username:
            return JsonResponse({"status_code": 2, "error_info": "username empty"})

        password = request.POST.get('password')
        if not password:
            return JsonResponse({"status_code": 3, "error_info": "password empty"})

        user_find = User.objects.filter(username=username)
        if user_find: # username exist
            return JsonResponse({"status_code": 1, "error_info": "username exists"})
        else: # success
            User.objects.create_user(username, password=password)
            return JsonResponse({"status_code": 0, "username": username})
    return HttpResponse("Please use POST method to signup.")

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username: # username empty
            return JsonResponse({"status_code": 2, "error_info": "username empty"})
        password = request.POST.get('password')
        if not password: # password empty
            return JsonResponse({"status_code": 3, "error_info": "password empty"})
        login_user = User.objects.filter(username=username)
        if login_user:
            user = authenticate(username=username, password=password)
            if user is None: # password incorrect
                return JsonResponse({"status_code": 1, "error_info": "password incorrect"})
            # delete old token
            old_token = Token.objects.filter(user=user)
            old_token.delete()

            token = Token.objects.create(user=user)
            # success
            return JsonResponse({
                "status_code": 0,
                "token": token.key,
                "username": user.username
                })
        else:  # username not exist
            return JsonResponse({"status_code": 4, "error_info": "username not exist"})
    return HttpResponse("Please use POST method to login.")