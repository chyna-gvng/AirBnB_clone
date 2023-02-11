#!/usr/bin/python3
"""
    Defines unittests for 'models/city.py'
    Unittest classes:
        TestCity_instantiation
        TestCity_save
        TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """
        Unittests to test instantiation of the 'City' class.
    """

    # 1. We’re importing the unittest module.
    # 2. We’re creating a class called TestCity that,
    # inherits from unittest.TestCase.
    # 3. We’re creating a method called test_no_args_instantiates,
    # that takes self as an argument.
    # 4. We’re using the assertEqual method to test that the type,
    # of City() is equal to the type of City.
    def test_no_args_instantiates(self):
        # It checks if the class City is the same type as,
        # the instance of the class City.
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        # It checks if the City object is in the storage.
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        # It checks that the id of the city is a string.
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        # It checks that the created_at attribute of the City class,
        # is an instance of the datetime class.
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        # It tests that the updated_at attribute of the City class,
        # is an instance of the datetime class.
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        # 1. We’re creating a new class called City.
        # 2. We’re creating a new instance of City called cy.
        # 3. We’re checking that the type of cy.state_id is str.
        # 4. We’re checking that the attribute state_id is,
        # in the directory of cy.
        # 5. We’re checking that the attribute state_id is,
        # not in the dictionary of cy.
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        # 1. We’re creating a class called City.
        # 2. We’re creating a class variable called name.
        # 3. We’re creating an instance of the City class called cy.
        # 4. We’re checking that the name class variable is a string.
        # 5. We’re checking that the name class variable,
        # is in the class’s directory.
        # 6. We’re checking that the name class variable,
        # is not in the class’s dictionary.
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        # 1. We create a new City object and assign it to cy1.
        # 2. We create a new City object and assign it to cy2.
        # 3. We check that the id of cy1 is not equal to the id of cy2.
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        # 1. We import the unittest module.
        # 2. We import the City class from the models.py file.
        # 3. We create a new class called TestCity that,
        # inherits from unittest.TestCase.
        # 4. We create a new method called test_has_name.
        # 5. We create a new City instance called “city”.
        # 6. We check that the name of the city is “San Francisco”.
        # 7. We create a new method called test_has_state_code.
        # 8. We create a new City instance called “city”.
        # 9. We check that the state_code of the city is “CA”.
        # 10. We create a new method called test_created_at_auto_assigned.
        # 11. We create a new City instance called “cy1”.
        # 12. We wait 0.05 seconds.
        # 13. We create a new City instance called “cy2”.
        # 14. We check that the created_at attribute of cy1,
        # is less than the created_at attribute of cy2.
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        # 1. We create a new City object and store it in cy1.
        # 2. We wait for 0.05 seconds.
        # 3. We create a new City object and store it in cy2.
        # 4. We check that the updated_at attribute of cy1,
        # is less than the updated_at attribute of cy2.
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        # 1. We create a datetime object and store it in the variable dt.
        # 2. We create a City object and store it in the variable cy.
        # 3. We set the id attribute of cy to “123456”.
        # 4. We set the created_at and updated_at attributes of cy,
        # to the datetime object we created in step 1.
        # 5. We call the __str__ method of cy and store the result,
        # in the variable cystr.
        # 6. We check that the string representation of cy contains,
        # the string “[City] (123456)”.
        # 7. We check that the string representation of cy contains,
        # the string “‘id’: ‘123456’”.
        # 8. We check that the string representation of cy contains,
        # the string “‘created_at’: ” followed by the string representation,
        # of the datetime object we created in step 1.
        # 9. We check that the string representation of cy contains,
        # the string “‘updated_at’: ” followed by the string representation,
        # of the datetime object we created in step 1.
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    def test_args_unused(self):
        # 1. We create a new City object, and pass in,
        # None as the value for the name attribute.
        # 2. We then check that the name attribute of,
        # the City object is not None.
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        # 1. We import the datetime module from the datetime library.
        # 2. We create a datetime object using the datetime.today() method.
        # 3. We convert the datetime object to a string,
        # using the isoformat() method.
        # 4. We create a City object with the id, created_at,
        # and updated_at attributes.
        # 5. We test that the id, created_at, and updated_at,
        # attributes are equal to the expected values.
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        # 1. We’re importing the unittest module.
        # 2. We’re importing the class we want to test.
        # 3. We’re creating a class called TestStringMethods,
        # that inherits from unittest.TestCase.
        # 4. We’re creating a method called test_upper.
        # 5. We’re using the self.assertEqual method to check,
        # if the result of the upper method is equal to ‘FOO’.
        # 6. We’re using the self.assertTrue method to check,
        # if the result of the isupper method is True.
        # 7. We’re using the self.assertFalse method to check,
        # if the result of the isupper method is False.
        # 8. We’re using the self.assertRaises method to check,
        # if the upper method raises a TypeError when the argument is None.
        # 9. We’re running the tests with unittest.main().
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """
        Unittests to test save method of the 'City' class.
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
        # 1. Create a new City object
        # 2. Sleep for 50 milliseconds
        # 3. Save the City object
        # 4. Assert that the updated_at field is,
        # greater than the first_updated_at field
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        # 1. Create a new City object.
        # 2. Save the object to the database.
        # 3. Update the object.
        # 4. Save the object to the database again.
        # 5. Assert that the updated_at field of the object has changed.
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        # 1. We create a new instance of City.
        # 2. We call the save() method with None as an argument.
        # 3. We check that the save() method raises a TypeError.
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        # 1. Create a new City object
        # 2. Save it to the database
        # 3. Open the file.json file
        # 4. Check if the city id is in the file
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """
        Unittests for testing 'to_dict' method of the 'City' class.
    """

    def test_to_dict_type(self):
        # It checks if the type of the return,
        # value of the to_dict method is a dictionary.
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
