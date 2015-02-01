import unittest
from mysite import MySite


class TestMySite(unittest.TestCase):
    def setUp(self):
        self.site = MySite()

    def test_index(self):
        index = self.site.index()
        self.assertIsInstance(index, str)

if __name__ == '__main__':
    unittest.main()
