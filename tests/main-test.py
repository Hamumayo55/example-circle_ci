import unittest
from src.main import add

class MainTest(unittest.TestCase):
    def test_add(self):
        ans = add(2,3)
        expected = 4
        self.assertEqual(ans, expected)
