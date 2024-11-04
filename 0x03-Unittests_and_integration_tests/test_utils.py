#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
import unittest.mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """0. Parameterize a unit test"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Parameterize a unit test"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """1. Parameterize a unit test"""
        with self.assertRaises(expected) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """2. Mock HTTP calls"""
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)
