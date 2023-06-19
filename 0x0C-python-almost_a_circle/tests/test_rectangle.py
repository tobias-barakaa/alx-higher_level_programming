import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_valid_attributes(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(5, 5, 1, 2, 100)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        self.assertEqual(r2.id, 100)

    def test_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_height(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_x(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_invalid_y(self):
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, 0, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle("10", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, [2])
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2, {})
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 2, 0, "1")
        self.assertEqual(str(context.exception), "y must be an integer")
    def setUp(self):
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__
    def test_display(self):
        # Create a rectangle with width 4 and height 6
        r1 = Rectangle(4, 6)
        # Capture the output of the display method
        r1.display()
        output = sys.stdout.getvalue().strip()
        expected_output = "####\n####\n####\n####\n####\n####"
        self.assertEqual(output, expected_output)

        # Reset the output buffer
        sys.stdout = StringIO()

        # Create a rectangle with width 2 and height 2
        r2 = Rectangle(2, 2)
        # Capture the output of the display method
        r2.display()
        output = sys.stdout.getvalue().strip()
        expected_output = "##\n##"
        self.assertEqual(output, expected_output)
    def test_update(self):
        r = Rectangle(2, 3, 1, 1, 10)
        r.update(20)
        self.assertEqual(r.id, 20)

        r.update(20, 5)
        self.assertEqual(r.width, 5)

        r.update(20, 5, 10)
        self.assertEqual(r.height, 10)

        r.update(20, 5, 10, 2)
        self.assertEqual(r.x, 2)

        r.update(20, 5, 10, 2, 4)
        self.assertEqual(r.y, 4)

        r.update()
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 4)

        r.update(30, 6, 12, 3, 5)
        self.assertEqual(r.id, 30)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 5)
   


if __name__ == "__main__":
    unittest.main()
