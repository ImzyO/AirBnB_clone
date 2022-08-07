#!/usr/bin/python3
"""Unittest for base model module.
"""
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel
baseModel = BaseModel()


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""
    def test_id_is_string(self):
        """UUID format testing.
        This test is designed to check if any generated UUID
        is correctly generated and has the propper format.
        """
        self.assertIsInstance(baseModel, str)

    def test_uuid_good_format(self):
        """
        Tests if UUID is in the correct format.
        """
        self.assertIsInstance(uuid.UUID(baseModel.id), uuid.UUID)

    def test_uuid_wrong_format(self):
        """
        Tests a badly named UUID, to confirm that it is checked.
        """
        baseModel.id = 'Monty Python'
        warn = 'badly formed hexadecimal UUID string'

        with self.assertRaises(ValueError) as msg:
            uuid.UUID(baseModel.id)

        self.assertEqual(warn, str(msg.exception))

    def test_uuid_version(self):
        """
        Tests if the version of the UUID is 4
        """
        conv_uuid = uuid.UUID(baseModel.id)

        self.assertEqual(conv_uuid.version, 4)

    def test_different_uuid(self):
        """
        checks id UUID are different when different objects are created.
        """
        bm_one = BaseModel()
        bm_two = BaseModel()
        conv_uuid_one = uuid.UUID(bm_one.id)
        conv_uuid_two = uuid.UUID(bm_two.id)

        self.assertNotEqual(conv_uuid_one, conv_uuid_two)

    def test_created_at_cls(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class was created are correctly assigned.
        """
        self.assertEqual(type(baseModel.created_at), datetime)

    def test_updated_at_cls(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class is updated are correctly assigned.
        """
        self.assertEqual(type(baseModel.updated_at), datetime)

    def test_construction_from_dictionary(self):
        """ This function proves that when passing a dictionary with
            extra attributes, these are added correctly
        """

        dict_t = {"id": "7734cf23-6c89-4662-8483-284727324c77",
                  "created_at": "2020-02-17T16:32:39.023915",
                  "updated_at": "2020-02-17T16:32:39.023940",
                  "__class__": "BaseModel"}

        x = dict_t["created_at"]
        y = dict_t["updated_at"]
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        my_base = BaseModel(**dic)

        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(my_base.created_at, datetime.strptime(x, time_format))
        self.assertEqual(my_base.updated_at, datetime.strptime(y, time_format))

    def test_init(self):
        """Test __init__
        """
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_to_dict(self):
        """test that values in dict returned from to_dict are correct"""
        dt = baseModel.to_dict()

        self.assertEqual(dt["id"], baseModel.id)
        self.assertEqual(dt["created_at"], baseModel.created_at.isoformat())
        self.assertEqual(dt["updated_at"], baseModel.updated_at.isoformat())
        self.assertEqual(dt["__class__"], "BaseModel")

        self.assertEqual(type(test_dict["__class__"]), str)
        self.assertEqual(type(test_dict["id"]), str)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)

    def test_documentation(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_methods(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test__init__(self):
        """test if the base is an instance of type BaseModel"""
        self.assertEqual(type(baseModel), BaseModel)

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_save(self):
        """test if the save method works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)


if __name__ == "__main__":
    unittest.main()
