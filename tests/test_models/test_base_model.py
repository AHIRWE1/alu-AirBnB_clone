#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_instance_creation(self):
        """Test instance is created with correct attributes"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method output"""
        obj = BaseModel()
        output = str(obj)
        self.assertIn("[BaseModel]", output)
        self.assertIn(obj.id, output)

    def test_save_method(self):
        """Test save updates updated_at"""
        obj = BaseModel()
        old_updated = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated, obj.updated_at)

    def test_to_dict_method(self):
        """Test to_dict returns correct dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()