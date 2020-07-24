from . import views
from django.urls import path


urlpatterns = [
    path('products', views.products_list),
    path('products/bulk_insert', views.products_add),
]

