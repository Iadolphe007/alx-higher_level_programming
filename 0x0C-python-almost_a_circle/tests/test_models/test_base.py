import unittest
import json
import csv
from models.base import Base
from models.square import Square
"""create test for models"""

class testBase(unittest.TestCase):
    def test_id_none(self):
        """test for no id"""
        base = Base()
        self.assertEqual(1, base.id)

    def test_id(self):
        """test for valid id"""
        base = Base(4)
        self.assertEqual(4, base.id)

    def test_id_zero(self):
        """test for zero id"""
        base = Base(0)
        self.assertEqual(0, base.id)

    def test_id_negative(self):
        """test for a negative id"""
        base = Base(-5)
        self.assertEqual(-5, base.id)

    def test_id_string(self):
        """test for string id"""
        base = Base("string")
        self.assertEqual("string", base.id)

    def test_id_list(self):
        """test wehn id is a list"""
        base = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], base.id)

    def test_id_dict(self):
        """test when id is a dictionary"""
        base = Base({"id": 7})
        self.assertEqual({"id":7}, base.id)

    def test_id_tuple(self):
        """test when id is a tuple"""
        base = Base((1,))
        self.assertEqual((1,), base.id)
    def test_to_json_type(self):
        """test json string"""
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_value(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([None])
        self.assertEqual(json_string, "[null]")

    def test_to_json_Empty(self):
        square = Square(1, 0, 0, 609)
        json_dict = square.to_dictionary()
        json_string = Base.to_json_string([None])
        self.assertEqual(json_string, "[null]")

class TestSquare(unittest.TestCase):
    """
    class for testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
if __name__ == '__main__':
    unittest.main()
