from django.test import TestCase
from django.urls import reverse


# https://docs.djangoproject.com/en/1.11/intro/tutorial05/

class WebsiteTests(TestCase):
    def test_is_home_working(self):
        response = self.client.get(reverse('frontend:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Home')

    def test_is_about_working(self):
        response = self.client.get(reverse('frontend:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Avi Aryan')
