from django.test import TestCase
from shop.models import *


class TestModels(TestCase):
    def test_category(self):
        category1 = Category.objects.create(name="Home and Living", slug="home", desc="demo")
        self.assertEquals(str(category1), "Home and Living")
        self.assertTrue(isinstance(category1, Category))
