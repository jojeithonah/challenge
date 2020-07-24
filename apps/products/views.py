from django.shortcuts import render

from django.http import JsonResponse
from . import models
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.utils import IntegrityError
from django.db import DataError
from django.core.exceptions import ValidationError
from .forms import ProductForm

def products_list(request):
    if request.method == 'GET':
        items = models.Product.objects.all().values()
        data = {"products": list(items)}
        return JsonResponse(data,status=200)

@csrf_exempt    
def products_add(request):
    if request.method == 'POST':
        errors_data = []
        products = json.loads(request.body)
        products = products.get('products')
        for product in products:
            form = ProductForm(product)
            if form.is_valid():
                form.save()
            else:
                errors = []
                for err in [json.loads(form.errors.as_json())]:
                    if err.get('value'):
                        errors.append("Key 'value': {}".format(err.get('value')[0]['message']))
                    if err.get('id'):
                        errors.append("Key 'id': {}".format(err.get('id')[0]['message']))
                    if err.get('__all__'):
                        errors.append("Key 'discount': {}".format(err.get('__all__')[0]['message']))
                    if err.get('stock'):
                        errors.append("Key 'stock': {}".format(err.get('stock')[0]['message']))
                errors_item = {
                    "product_id": product['id'],
                    "errors": errors
                }
                errors_data.append(errors_item)
        if errors_data:
            return JsonResponse(dict(products_report=errors_data),status=200)
        return JsonResponse(dict(status="OK"),status=200)
    
