from django.shortcuts import render

from django.http import JsonResponse
from . import models
from django.core import serializers

def get_hello(request):
    if request.method == 'GET':
        items = models.Product.objects.all().values()
        data = {"products": list(items)}
        return JsonResponse(data,status=200)