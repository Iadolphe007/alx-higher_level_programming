import unittest
from models.rectangle import Rectangle
"""test rectangle"""


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """set upp rectangle"""
        self.rectangle = Rectangle(10, 5, 2, 3, 1)

    def test_attributes(self):
        """test rectangle attr"""
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 5)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_invalid_width(self):
        """test invalid width"""
        with self.assertRaises(ValueError):
            self.rectangle.width = 0
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"

    def test_invalid_height(self):
        """test invalid height"""
        with self.assertRaises(ValueError):
            self.rectangle.height = -5
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"

    def test_invalid_x(self):
        """test when x is invalid"""
        with self.assertRaises(ValueError):
            self.rectangle.x = -2
        with self.assertRaises(TypeError):
            self.rectangle.x = "invalid"

    def test_invalid_y(self):
        """test when y is invalid"""
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"

    def test_area(self):
        """test area model"""
        self.assertEqual(self.rectangle.area(), 50)

    def test_display(self):
        """test display model"""
        self.rectangle.display()

    def test_to_dictionary(self):
        """test to dictianary model"""
        expected_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_update_kwargs(self):
        """test updated kwargs"""
        self.rectangle.update(x=4, y=2)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 2)


if __name__ == '__main__':
    unittest.main()
