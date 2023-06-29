#!/usr/bin/python3


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0_id_None(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_1_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(11)
        b4 = Base(-12)
        b5 = Base(0)
        b6 = Base(1.1)
        b7 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 11)
        self.assertEqual(b4.id, -12)
        self.assertEqual(b5.id, 0)
        self.assertEqual(b6.id, 1.1)
        self.assertEqual(b7.id, 3)

    def test_2_id_single(self):
        b1 = Base(3)
        self.assertEqual(b1.id, 3)

    def test_3_id_multi(self):
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        b2 = Base(4)
        self.assertEqual(b2.id, 4)

    def test_4_id_string(self):
        b1 = Base("foo")
        self.assertEqual(b1.id, "foo")

    def test_5_id_NaN(self):
        b1 = Base(float("nan"))
        self.assertNotEqual(b1.id, float("nan"))

    def test_6_id_sameId(self):
        b1 = Base(22)
        self.assertEqual(b1.id, 22)
        b2 = Base(22)
        self.assertEqual(b2.id, 22)

    def test_7_to_json_string(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([{"id": 1, "name": "foo"},
                                           {"id": 2, "name": "bar"}])
        self.assertEqual(json_string, '[{"id": 1, "name": "foo"},\
 {"id": 2, "name": "bar"}]')

    def test_8_save_to_file(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

        Square.save_to_file(None)
        self.assertTrue(os.path.isfile("Square.json"))
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_9_from_json_string(self):
        json_string = '[]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

        json_string = '[{"id": 1, "name": "foo"}, {"id": 2, "name": "bar"}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1, "name": "foo"},
                                  {"id": 2, "name": "bar"}])

        
if __name__ == '__main__':
        unittest.main()
