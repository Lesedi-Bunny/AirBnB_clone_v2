#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
from console import HBNBCommand


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestCreateState(unittest.TestCase):
    """
    tests create command
    """
    def test_ceate_state(self):
        """
        test creation of state objects
        """
        cmd = HBNBCommand()
        cmd.onecmd('create State name="California"')

        self.assertEqual(State.name, "California")
