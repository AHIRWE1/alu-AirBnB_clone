#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel


class TestBaseModelSaveReload(unittest.TestCase):
    def test_new_object_is_saved(self):
        my_model = BaseModel()
        my_model.name = "Test_Model"
        my_model.my_number = 42
        my_model.save()
        key = f"BaseModel.{my_model.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Test_Model")
        self.assertEqual(storage.all()[key].my_number, 42)

    def test_reload_objects(self):
        storage.reload()
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        for obj in objects.values():
            self.assertIsInstance(obj, BaseModel)

if __name__ == "__main__":
    unittest.main()
