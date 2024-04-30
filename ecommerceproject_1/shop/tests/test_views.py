from django.test import TestCase, Client
from django.urls import reverse, resolve


class TestViews(TestCase):
    def test_home(self):
        client = Client()
        response = client.get(reverse('home'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
