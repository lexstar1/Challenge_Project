from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blue.views import code, test

class TestUrls(SimpleTestCase):

    def test_health_url_is_resolved(self):
        url = reverse('health')
        print(resolve(url))

    def test_secret_url_is_resolved(self):
        url = reverse('secret')
        print(resolve(url))

