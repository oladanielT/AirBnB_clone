#!/usr/bin/python3
"""
model to test my base model
"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    module to test
    """
    def test_init(self):
        test_model = BaseModel()

        self.assertIsNotNone(test_model.id)
        self.assertIsNotNone(test_model.created_at)
        self.assertIsNotNone(test_model.updated_at)

    def test_save(self):
        """
        testing saved updated time
        """
        test_model = BaseModel()
        self.assertNotEqual(test_model.save(), test_model.updated_at)

    def test_dict(self):
        test_model = BaseModel()
        test_model_dict = test_model.to_dict()

        self.assertIsInstance(test_model_dict, dict)
        self.assertEqual(test_model_dict["__class__"], "BaseModel")
        self.assertEqual(test_model_dict["created_at"], test_model.created_at.isoformat())
        self.assertEqual(test_model_dict["updated_at"], test_model.updated_at.isoformat())
        self.assertEqual(test_model_dict["id"], test_model.id)

    def test_str(self):
        test_model = BaseModel()
        self.assertTrue(str(test_model).startswith("[BaseModel]"))
        self.assertIn(str(test_model.id), str(test_model))
        self.assertIn(str(test_model.__dict__), str(test_model))

if __name__ == "__main__":
    unittest.main()
