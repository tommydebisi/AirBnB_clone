#!/usr/bin/python3
"""
    Tests for Base Model Module
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime as dt


class TestBaseModelDict(unittest.TestCase):
    """
        Test class for Base Model Dict
    """

    def test_created_updated_type(self):
        """
            Checks for the types of created at and updated at
            before an after passed as a kwarg
        """

        mod1 = BaseModel()
        mod_dic = mod1.to_dict()

        self.assertIs(type(mod_dic.get('created_at')), str)
        self.assertIs(type(mod_dic.get('updated_at')), str)

        new_mod = BaseModel(**mod_dic)

        self.assertIs(type(new_mod.created_at), dt)
        self.assertIs(type(new_mod.updated_at), dt)

    def test_for_attr_class(self):
        """
            Checks if the attribute 'class' is present in the newly
            created instance
        """

        mod1 = BaseModel()  
        mod_dic = mod1.to_dict()
        new_mod = BaseModel(**mod_dic)

        self.assertFalse(new_mod.__dict__.get('__class__'))
