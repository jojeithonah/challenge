from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError 

# Create your models here.

class Product(models.Model):    
    id = models.CharField(
        _("Identifier"), 
        max_length=255,
        primary_key=True
        )
    name = models.CharField(
        _("Name"), 
        max_length=55,
        validators=[MinLengthValidator(3),MaxLengthValidator(55)]
        )
    value = models.FloatField(
        _("Value"),
        validators=[MinValueValidator(1),MaxValueValidator(99999.8)]
        )
    discount_value = models.FloatField(
        _("Discount Value"),
        null=True,
        blank=True,
        )
    stock = models.PositiveIntegerField(
        _("Stock")
        )
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural  = 'Products'
        
    def clean(self):
        super(Product, self).clean()
        if self.value  and self.discount_value:
            if self.discount_value >= self.value:
                raise ValidationError(_('Invalid discount value'))
    
    def __unicode__(self):
        return self.name
