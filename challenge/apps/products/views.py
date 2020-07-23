from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
# Create your models here.


def get_hello(request):
    if request.method == 'GET':
        return JsonResponse(dict(data="holaa"),status=200)