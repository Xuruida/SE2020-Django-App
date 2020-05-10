from django.shortcuts import render

# JsonResponse
from django.http import HttpResponse, JsonResponse
# User
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

# Auth
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
# Create your views here.

import re

@csrf_exempt
@api_view(['POST', 'GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def holiday(request):
    if request.method == 'POST':
        query_date = request.POST.get('date')
        if not query_date:
            return JsonResponse(
                {
                    "status_code": 2,
                    "error_info": "param date does not exist"
                })
        match = re.match('[0-9]{4}\-[0-9]{2}\-[0-9]{2}', query_date)
        if not match:
            return JsonResponse(
                {
                    "status_code": 3,
                    "error_info": "Date format invalid. Please provide format: YYYY-MM-DD"
                })
        year, month, day = map(int, query_date.split('-'))
        holiday_name = ''
        if (month == 10 and day == 1):
            holiday_name = '国庆节'
        elif (month == 12 and day == 25):
            holiday_name = '圣诞节'
        elif (month == 1 and day == 1):
            holiday_name = '元旦'
        if (len(holiday_name) == 0):
            return JsonResponse({})
        else:
            return JsonResponse(
                {
                    "status_code": 0,
                    "error_info": holiday_name
                }, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({"status_code": -1, "error_info": "Please use POST method to check holidays."})