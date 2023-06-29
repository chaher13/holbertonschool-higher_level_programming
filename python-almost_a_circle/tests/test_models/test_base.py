import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
import os
import json


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

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertIsInstance(json_dictionary, str)
        expected_json = '[{"id": 6, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_dictionary, expected_json)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json", "r") as file:
            json_content = json.load(file)

        expected_json = [{"y": 8, "x": 2, "id": 4, "width": 10, "height": 7},\
                         {"y": 0, "x": 0, "id": 5, "width": 2, "height": 4}]
        self.assertEqual(json_content, expected_json)

        os.remove("Rectangle.json")

        def test_from_json_string(self):
            list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
            ]
            json_list_input = Rectangle.to_json_string(list_input)
            list_output = Rectangle.from_json_string(json_list_input)

            self.assertEqual(type(list_input), list)
            self.assertEqual(type(json_list_input), str)
            self.assertEqual(type(list_output), list)
            self.assertEqual(list_output, list_input)

        def test_create_rectangle(self):

            r1 = Rectangle(3, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(**r1_dictionary)

            self.assertEqual(r1.width, r2.width)
            self.assertEqual(r1.height, r2.height)
            self.assertEqual(r1.x, r2.x)
            self.assertEqual(r1.y, r2.y)

            self.assertIsNot(r1, r2)


if __name__ == '__main__':
    unittest.main()
