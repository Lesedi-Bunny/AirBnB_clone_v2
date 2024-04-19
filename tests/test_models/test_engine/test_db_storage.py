#!/usr/bin/python3
"""
test cases for DB storage class
"""

import os
import unittest
from models import storage
from models.engine.db_storage import DBStorage
from models.state import State


@unittest.skipIf(storage_type != "db" and env != "test", "Skipping file tests")
class TestDBStorage(unittest.TestCase):
    """
    Test the DBStorage class
    """

    def setUp(self):
        """
        Set up for the tests
        """
        storage.rollback()
        storage.drop_all()
        storage.reload()

    def test_all(self):
        """Test if 'all' returns the dictionary"""
        obj = storage.all()
        self.assertIsInstance(obj, dict)
        self.assertTrue(len(obj) == 0)

    def test_new(self):
        """
        Test 'new '
        """
        state = State(name="Bloemfontein")
        storage.new(state)
        self.assertIn(state, storage.all().values())

    def test_save(self):
        """
        Test 'save'
        """
        state = State(name="Bloemfontein")
        storage.new(state)
        storage.save()
        self.assertIn(state, storage.all().values())

    def test_delete(self):
        """
        Test 'delete'
        """
        state = State(name="Bloemfontein")
        storage.new(state)
        storage.save()
        storage.delete(state)
        self.assertNotIn(state, storage.all().values())

    def test_reload(self):
        """
        Test 'reload'
        """
        state = State(name="Bloemfontein")
        storage.new(state)
        storage.save()
        storage.reload()
        self.assertNotIn(state, storage.all().values())
