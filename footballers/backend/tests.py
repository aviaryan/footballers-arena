from django.test import TestCase
from django.urls import reverse
from .models import Footballer

# https://docs.djangoproject.com/en/1.11/intro/tutorial05/

class FootballerModelTests(TestCase):
    def test_is_model_empty_friendly(self):
        footballer = Footballer(name='Ronaldo')
        self.assertEqual(str(footballer), 'Ronaldo')


class BackendViewTests(TestCase):
    def test_root_page(self):
        response = self.client.get(reverse('backend:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'API')
