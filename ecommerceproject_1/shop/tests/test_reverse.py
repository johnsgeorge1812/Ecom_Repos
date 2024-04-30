from django.test import TestCase
from django.urls import reverse, resolve
from shop.views import *


class TestURL(TestCase):
    def Testhome(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
