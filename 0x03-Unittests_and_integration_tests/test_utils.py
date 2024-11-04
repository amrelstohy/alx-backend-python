#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
import unittest.mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Parameterize and patch"""

    def test_memoize(self):
        """3. Parameterize and patch"""

        class TestClass:
            """class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with unittest.mock.patch.object(
                                        TestClass,
                                        'a_method',
                                        return_value=42) as mock_method:
            obj = TestClass()

            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)

            mock_method.assert_called_once()
