""" Test Client """
import unittest

from testlodge import Client


class TestClient(unittest.TestCase):
    """ Test Client """

    def test_initialization(self) -> None:
        _ = Client(
            email='test@email.com',
            api_key='aslkdjf342DKLFJSAF324',
            account_id=9487234,
        )

    def test_paths(self) -> None:
        """ Test the client paths. """
        client = Client(
            email='test@email.com',
            api_key='aslkdjf342DKLFJSAF324',
            account_id=9487234,
        )

        self.assertEqual(
            client.base_url, 'https://api.testlodge.com/v1/account/9487234'
        )
