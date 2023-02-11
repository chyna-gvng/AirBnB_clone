#!/usr/bin/python3
"""
    Defines unittests for 'models/amenity.py'
    Unittest classes:
        TestAmenity_instantiation
        TestAmenity_save
        TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
        Unittests to test instantiation of the 'Amenity' class.
    """

    def test_no_args_instantiates(self):
        # It checks if the class Amenity is the same type as,
        # the instance of the class Amenity.
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        # It checks if the Amenity class is in the storage.
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        # It checks that the id of the Amenity class is a string.
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        # It checks if the type of the created_at attribute is datetime
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        # It checks if the type of the updated_at attribute is datetime.
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        # 1. We’re creating a new class called Amenity.
        # 2. We’re creating a new instance of Amenity called am.
        # 3. We’re checking that the type of the name attribute is a string.
        # 4. We’re checking that the name attribute is in the Amenity class.
        # 5. We’re checking that the name attribute is not in the am instance.
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        # 1. We create two instances of the Amenity class.
        # 2. We check that the id of each instance is different.
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        # 1. We create an instance of Amenity.
        # 2. We wait 0.05 seconds.
        # 3. We create another instance of Amenity.
        # 4. We check that the first instance was created before the second.
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        # 1. We create a new instance of Amenity.
        # 2. We wait 0.05 seconds.
        # 3. We create a second instance of Amenity.
        # 4. We check that the updated_at attribute of the first instance,
        # is less than the updated_at attribute of the second instance.
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        # 1. We create a datetime object and store it in dt.
        # 2. We create a string representation of dt and store it in dt_repr.
        # 3. We create an Amenity object and store it in am.
        # 4. We set the id attribute of am to “123456”.
        # 5. We set the created_at and updated_at attributes of am to dt.
        # 6. We create a string representation of am and store it in amstr.
        # 7. We check that the string representation of am contains the string
        # “[Amenity] (123456)”.
        # 8. We check that the string representation of am contains the string
        # “‘id’: ‘123456’”.
        # 9. We check that the string representation of am contains the string
        # “‘created_at’: ” followed by the string representation of dt.
        # 10. We check that the string representation of am contains the string
        # “‘updated_at’: ” followed by the string representation of dt.
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        # 1. We create a new instance of Amenity.
        # 2. We check that the instance’s __dict__ does not contain,
        # None as a value.
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
            instantiation with kwargs test method
        """
        # 1. We import the datetime module from the datetime library.
        # 2. We create a datetime object using the datetime.today() method.
        # 3. We convert the datetime object to a string,
        # using the isoformat() method.
        # 4. We create an Amenity object with the id “345” and,
        # the datetime object as the created_at and updated_at attributes.
        # 5. We check that the id is “345”.
        # 6. We check that the created_at attribute is a datetime object.
        # 7. We check that the updated_at attribute is a datetime object.
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        # 1. We import the unittest module.
        # 2. We import the class we want to test.
        # 3. We create a class called TestStringMethods that inherits,
        # from unittest.TestCase.
        # 4. We create a method called test_upper.
        # 5. We use the self.assertEqual method to check if the result,
        # of the upper method applied to ‘foo’ is equal to ‘FOO’.
        # 6. We use the self.assertTrue method to check if the result,
        # of the isupper method applied to ‘FOO’ is True.
        # 7. We use the self.assertFalse method to check if the result,
        # of the isupper method applied to ‘Foo’ is False.
        # 8. We use the self.assertEqual method to check if the result,
        # of the split method applied to ‘hello world’ is,
        # equal to ['hello', 'world'].
        # 9. We use the self.assertRaises method to check if the result,
        # of the split method applied to ‘hello world’ raises a TypeError.
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """
        Unittests to test save method of the 'Amenity' class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        # 1. Create a new instance of Amenity
        # 2. Save the current time in a variable
        # 3. Save the instance of Amenity
        # 4. Compare the current time with,
        # the updated_at attribute of the instance
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        # 1. Create a new instance of Amenity
        # 2. Save it to the database
        # 3. Update the instance with new data
        # 4. Save it to the database again
        # 5. Assert that the updated_at field was updated
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
        Unittests to test to_dict method of the 'Amenity' class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
