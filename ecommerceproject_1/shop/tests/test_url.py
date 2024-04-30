from django.test import TestCase


class TestURl(TestCase):
    def testhome(self):
        result = self.client.get('/')
        self.assertEquals(result.status_code, 200)
