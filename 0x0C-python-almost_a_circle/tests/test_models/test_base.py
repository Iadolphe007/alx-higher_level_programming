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

    def test_to_json_string(self):
        """
        test if to_json_string returns the
        correct JSON representation
        """
        list_dictionaries = [{'id': 1, 'name': 'John'},
                {'id': 2, 'name': 'Alice'}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]')

    def test_save_to_file(self):
        """ Test if save_to_file correctly saves the 
        JSON representation to a file
        """
        list_objs = [Base(1), Base(2), Base(3)]
        Base.save_to_file(list_objs)
        with open('Base.json', 'r') as file:
            json_string = file.read()
            self.assertEqual(json_string, '[{"id": 1}, {"id": 2}, {"id": 3}]')

    def test_from_json_string(self):
        """Test if from_json_string correctly 
        converts JSON to Python objects
        """
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]'
        list_objs = Base.from_json_string(json_string)
        self.assertEqual(len(list_objs), 2)
        self.assertEqual(list_objs[0].id, 1)
        self.assertEqual(list_objs[1].id, 2)

    def test_create(self):
        """
        Test if create correctly creates and
        updates an object from a dictionary
        """
        dictionary = {'id': 1, 'name': 'John'}
        base = Base.create(**dictionary)
        self.assertEqual(base.id, 1)
        self.assertEqual(base.name, 'John')

    def test_load_from_file(self):
        """Test if load_from_file correctly loads objects from a file"""
        list_objs = [Base(1), Base(2), Base(3)]
        Base.save_to_file(list_objs)
        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 3)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[2].id, 3)

    def test_save_to_file_csv(self):
        """
        Test if save_to_file_csv correctly serializes a
        list of objects and saves them to a CSV file
        """
        list_objs = [Base(1), Base(2), Base(3)]
        Base.save_to_file_csv(list_objs)

        with open('Base.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
            self.assertEqual(len(rows), 3)
            self.assertEqual(int(rows[0]['id']), 1)
            self.assertEqual(int(rows[1]['id']), 2)
            self.assertEqual(int(rows[2]['id']), 3)
        """Test if save_to_file_csv handles empty list correctly"""
        empty_list = []
        Base.save_to_file_csv(empty_list)

        with open('Base.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
            self.assertEqual(len(rows), 1)

        """Test if save_to_file_csv handles None correctly"""
        Base.save_to_file_csv(None)

        with open('Base.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
            self.assertEqual(len(rows), 1)

    def test_load_from_file_csv(self):
        """test if load_from_file_csv correctly deserializes
        a CSV file and converts its contents into a list
        of Python objects
        """
        list_objs = [Base(1), Base(2), Base(3)]
        Base.save_to_file_csv(list_objs)

        loaded_objs = Base.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 3)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)
        self.assertEqual(loaded_objs[2].id, 3)

        """handle non existing object"""
        nonexistent_objs = Base.load_f
if __name__ == '__main__':
    unittest.main()
