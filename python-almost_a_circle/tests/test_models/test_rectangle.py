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
        with self.assertRaises(TypeError) as c:
            Rectangle(10, "2")
            self.assertEqual(str(c.exception), "height must be an integer")

    def test_width(self):
        with self.assertRaises(ValueError) as c:
            r = Rectangle(10, 2)
            r.width = -10
            self.assertEqual(str(c.exception), "width must be > 0")

    def test_x_type(self):
        with self.assertRaises(TypeError) as c:
            r = Rectangle(10, 2)
            r.x = {}
            self.assertEqual(str(c.exception), "x must be an integer")

    def test_y(self):
        with self.assertRaises(ValueError) as c:
            Rectangle(10, 2, 3, -1)
            self.assertEqual(str(c.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        expected_output = "####\n" * 6
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r1 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(expected_output, self.get_display_output(r1))

        r2 = Rectangle(2, 2)
        expected_output = "##\n" * 2
        captured_output = StringIO()
        sys.stdout = captured_output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        r2 = Rectangle(3, 2, 1, 0)
        expected_output = " ###\n ###\n"
        self.assertEqual(expected_output, self.get_display_output(r2))

    def get_display_output(self, rectangle):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            rectangle.display()
            output = out.getvalue()
            return output
        finally:
            sys.stdout = saved_stdout

    def test_str_representation(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")


if __name__ == '__main__':
    unittest.main()
