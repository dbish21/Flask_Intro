import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_welcome(self):
        response = self.app.get('/welcome')
        self.assertEqual(response.data.decode(), 'welcome')

    def test_welcome_home(self):
        response = self.app.get('/welcome/home')
        self.assertEqual(response.data.decode(), 'welcome home')

    def test_welcome_back(self):
        response = self.app.get('/welcome/back')
        self.assertEqual(response.data.decode(), 'welcome back')

if __name__ == '__main__':
    unittest.main()

