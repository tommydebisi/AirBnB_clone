#!/usr/bin/python3
"""
    Tests for console
"""

from io import StringIO
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestForConsole(unittest.TestCase):
    """
        class of console test
    """

    def test_create_base_model(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], BaseModel)

    def test_create_user(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], User)

    def test_create_state(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], State)

    def test_create_review(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Review)

    def test_create_place(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Place)

    def test_create_amenity(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Amenity)

    def test_create_city(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()  # string mangling
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], City)

    def test_for_missing_class_name(self):
        """
            tests for missing class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip("\n"), "** class name missing **")

    def test_for_wrong_class_name(self):
        """
            tests for the wrong class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create mymodel")
            self.assertEqual(f.getvalue().strip("\n"), "** class doesn't exist **")

    def test_show_base_model(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "BaseModel.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_help_for_create_command(self):
        """
        tests help string for create command
        """

        hlp_string = "create a new instance of an object\nUsage: create <class name>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip("\n"), hlp_string)

    def test_show_user(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "User.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_state(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "State.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_review(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Review.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_place(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Place.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_city(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "City.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_amenity(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Amenity.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_for_missing_class_name_show(self):
        """
            tests for missing class name using the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip("\n"), "** class name missing **")

    def test_for_wrong_class_name_show(self):
        """
            tests for the wrong class name using show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show mymodel")
            self.assertEqual(f.getvalue().strip("\n"), "** class doesn't exist **")

    def test_for_no_id_in_show_command(self):
        """
            tests for the wrong class name using show command
        """
        for key, value in classes.items():
            with patch('sys.stdout', new=StringIO()) as f:
                with self.subTest(key=key, value=value):
                    HBNBCommand().onecmd("show {}".format(value.__name__))
                    self.assertEqual(f.getvalue().strip("\n"), "** instance id missing **")
            
    def test_for_wrong_id(self):
        """
        tests if the id is valid
        """
        for key, value in classes.items():
            with patch('sys.stdout', new=StringIO()) as f:
                with self.subTest(key=key, value=value):
                    HBNBCommand().onecmd("show {} 111-745a-r78433".format(value.__name__))
                    self.assertEqual(f.getvalue().strip("\n"), "** no instance found **")

    def test_help_for_show_command(self):
        """
        tests help string for show command
        """

        hlp_string = "Prints the string rep. of an ins based on class name & id\nUsage: show <class name> <id>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip("\n"), hlp_string)

    def test_destroy_base_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "BaseModel.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))
    
    def test_destroy_user_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "User.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))
    
    def test_destroy_state_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "State.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))

    def test_destroy_reveiw_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Review.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))

    def test_destroy_place_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Place {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Place.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))

    def test_destroy_city_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "City.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))

    def test_destroy_amenity_model(self):
        """
            tests the destroy command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Amenity {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Amenity.{}".format(my_baseid)
            self.assertEqual(None, all_objs.get(k_string))
        
    def test_help_for_destroy_command(self):
        """
        tests help string for destroy command
        """

        hlp_string = "Deletes an instance based on the class name\nUsage: destroy <class name> <id>"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(f.getvalue().strip("\n"), hlp_string)


    def test_for_missing_class_name_destroy(self):
        """
            tests for missing class name using the destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip("\n"), "** class name missing **")

    def test_for_wrong_class_name_destroy(self):
        """
            tests for the wrong class name using destroy command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy mymodel")
            self.assertEqual(f.getvalue().strip("\n"), "** class doesn't exist **")

    def test_for_no_id_in_destroy_command(self):
        """
            tests for the wrong class name using destroy command
        """
        for key, value in classes.items():
            with patch('sys.stdout', new=StringIO()) as f:
                with self.subTest(key=key, value=value):
                    HBNBCommand().onecmd("destroy {}".format(value.__name__))
                    self.assertEqual(f.getvalue().strip("\n"), "** instance id missing **")
            
    def test_for_wrong_id(self):
        """
        tests if the id is valid
        """
        for key, value in classes.items():
            with patch('sys.stdout', new=StringIO()) as f:
                with self.subTest(key=key, value=value):
                    HBNBCommand().onecmd("destroy {} 111-745a-r78433".format(value.__name__))
                    self.assertEqual(f.getvalue().strip("\n"), "** no instance found **")


    def test_update_command(self):
        """test the update command"""

        attr = 'first_name'
        val = 'Betty'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} {} {}".format(my_baseid, attr, val))
            all_objs = storage.all()
            k_string = "BaseModel.{}".format(my_baseid)
            obj = all_objs.get(k_string)
            dic = obj.to_dict()
            self.assertIn(attr, dic.keys())

    def test_update_alone(self):
        """test the update command with no parameters passed"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip("\n"), "** class name missing **")

    def test_update_one_arg(self):
        """test the update command with one parameter passed"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip("\n"), "** instance id missing **")

    def test_update_two_arg(self):
        """test the update command with two parameter passed"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {}".format(my_baseid))
            self.assertEqual(f.getvalue().strip("\n"), "** attribute name missing **")

    def test_update_wrong_id(self):
        """test the update command with wrong id passed"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 19283799283")
            self.assertEqual(f.getvalue().strip("\n"), "** no instance found **")

    def test_update_two_arg(self):
        """test the update command with two parameter passed"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel {} first_name".format(my_baseid))
            self.assertEqual(f.getvalue().strip("\n"), "** value missing **")




class TestConsole(unittest.TestCase):
    """
    This test checks if all required classes
    are created correctly.
    """
    def test_class(self):
        """
        This test checks if all required classes
        are present
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        self.assertEqual(city1.__class__.__name__, "City")
        self.assertEqual(amenity1.__class__.__name__, "Amenity")
        self.assertEqual(state1.__class__.__name__, "State")
        self.assertEqual(rev1.__class__.__name__, "Review")
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """
        This test checks if all required classes
        inherit correcly from BaseModel
        """
        city1 = City()
        amenity1 = Amenity()
        state1 = State()
        rev1 = Review()
        place1 = Place()
        self.assertTrue(issubclass(city1.__class__, BaseModel))
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))
        self.assertTrue(issubclass(state1.__class__, BaseModel))
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
        self.assertTrue(issubclass(place1.__class__, BaseModel))

import console
import inspect
import pep8
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
