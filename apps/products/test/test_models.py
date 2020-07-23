from django.test import TestCase
from .. import models

class TestModels(TestCase):
    
    def create_product(self):
        return models.Product.objects.create(
            id = '12',
            name = 'tt',
            value = 123,
            discount_value = 12,
            stock = 0
        )

    def test_product_creation(self):
        w = self.create_product()
        self.assertTrue(isinstance(w, models.Product))
        self.assertEqual(w.__unicode__(), w.name)
