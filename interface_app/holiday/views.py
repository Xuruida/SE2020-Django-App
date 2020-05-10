from django.shortcuts import render

# JsonResponse
from django.http import HttpResponse, JsonResponse
# User
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication

import re
# Create your views here.

@csrf_exempt
def holiday(request):
   if request.method == 'POST':
       holiday_name = '国庆节'
       return JsonResponse({"status_code": 0, "error_info": holiday_name}, json_dumps_params={'ensure_ascii': False})
   return JsonResponse({"status_code": -1, "error_info": "Please use POST method to check holidays."})