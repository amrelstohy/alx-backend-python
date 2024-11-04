#!/usr/bin/env python3
"""Parameterize and patch as decorators"""
import unittest
import unittest.mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""

    @parameterized.expand(['google', 'abc'])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, mock_get):
        mock_get.return_value = 'test'

        obj = GithubOrgClient(org_name)
        self.assertEqual(obj.org, 'test')
        mock_get.assert_called_once()
