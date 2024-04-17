#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models import storage
import unittest


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


class TestPlaceCreation(unittest.TestCase):
    """
    test create command for place objects
    """
    def setUp(self):
        """
        set up the test environment
        """
        storage.new(Place)
        storage.save()

    def test_create_place(self):
        """
        test creating a place instance
        """
        new_place = Place(
            city_id="0001", user_id="0001", name="My_little_house",
            number_rooms=4, number_bathrooms=2,
            max_guest=10, price_by_night=300,
            latitude=37.773972, longitude=-122.431297
        )
        storage.save()

        place_from_storage = storage.all()[new_place.id]

        self.assertIsInstance(place_from_storage, Place)
        self.assertEqual(place_from_storage.city_id, "0001")
        self.assertEqual(place_from_storage.user_id, "0001")
        self.assertEqual(place_from_storage.name, "My little house")
        self.assertEqual(place_from_storage.number_rooms, 4)
        self.assertEqual(place_from_storage.number_bathrooms, 2)
        self.assertEqual(place_from_storage.max_guest, 10)
        self.assertEqual(place_from_storage.price_by_night, 300)
        self.assertEqual(place_from_storage.latitude, 37.773972)
        self.assertEqual(place_from_storage.longitude, -122.431297)
