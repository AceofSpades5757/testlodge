""" Test Client """
import unittest

from testlodge import Client


class TestClient(unittest.TestCase):
    """Test Client"""

    def setUp(self):
        self.client = Client(
            email='test@email.com',
            api_key='aslkdjf342DKLFJSAF324',
            account_id=9487234,
        )

    def test_paths(self) -> None:
        """Test the client paths."""

        client = self.client

        self.assertEqual(
            str(client.base_url),
            'https://api.testlodge.com/v1/account/9487234',
        )

    def test_path_interface(self) -> None:
        """Sanity checks for furl's path interface."""

        client = self.client

        self.assertEqual(
            str(client.base_url / 'resource' / 'show'),
            'https://api.testlodge.com/v1/account/9487234/resource/show',
        )
