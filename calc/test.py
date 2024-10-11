import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/math/add?a=10&b=20')
        self.assertEqual(response.data.decode(), '30.0')

    def test_sub(self):
        response = self.app.get('/math/sub?a=20&b=10')
        self.assertEqual(response.data.decode(), '10.0')

    def test_mult(self):
        response = self.app.get('/math/mult?a=10&b=5')
        self.assertEqual(response.data.decode(), '50.0')

    def test_div(self):
        response = self.app.get('/math/div?a=20&b=5')
        self.assertEqual(response.data.decode(), '4.0')

    def test_invalid_operation(self):
        response = self.app.get('/math/invalid?a=20&b=5')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
