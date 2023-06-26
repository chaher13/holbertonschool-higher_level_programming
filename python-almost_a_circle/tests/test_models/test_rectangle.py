import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(2, 10, 5, 3, 15)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 15)

        r3 = Rectangle(5, 5, id=25)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 25)

    def test_setters(self):
        r = Rectangle(10, 5)
        r.width = 5
        r.height = 10
        r.x = 2
        r.y = 2

        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_height_type(self):
        with self.assertRaises(TypeError) as context:
            Rectangle(10, "2")
            self.assertEqual(str(context.exception), "height must be an integer")

    def test_width(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2)
            r.width = -10
            self.assertEqual(str(context.exception), "width must be > 0")

    def test_x_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2)
            r.x = {}
            self.assertEqual(str(context.exception), "x must be an integer")

    def test_y(self):
        with self.assertRaises(ValueError) as context:
            Rectangle(10, 2, 3, -1)
            self.assertEqual(str(context.exception), "y must be >= 0")


    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ == '__main__':
    unittest.main()
