from . import models
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = '__all__'