from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_something(self):
        response = self.client.get('http://127.0.0.1/:8000')
        self.assertEqual(response.status_code, 404)
