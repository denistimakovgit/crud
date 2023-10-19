from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.
class TestSmth(TestCase):
    def test_sample_view_ok(self):
        client = APIClient()
        url = 'api/v1/products/'
        response = client.get(url)
        assert response.status_code == 404
