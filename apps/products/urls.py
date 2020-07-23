from . import views
from django.urls import path


urlpatterns = [
    path('products/', views.get_hello),
]

