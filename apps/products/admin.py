from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'discount_value', 'stock')
    search_fields = ['id', 'name', 'value','discount_value','stock']