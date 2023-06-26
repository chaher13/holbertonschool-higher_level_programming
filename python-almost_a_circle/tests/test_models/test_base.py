import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_iterid(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_explicitid(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()
