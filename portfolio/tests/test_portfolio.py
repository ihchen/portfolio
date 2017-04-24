import unittest

from portfolio import app

class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_has_my_name(self):
        rv = self.app.get('/')
        self.assertIn(b'Imanuel Chen', rv.data)
