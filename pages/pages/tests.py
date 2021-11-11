from django.http import response
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        return self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        return self.assertEqual(response.status_code,200)