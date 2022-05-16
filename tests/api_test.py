import unittest

from testlodge import SuiteSectionAPI


class TestAPI(unittest.TestCase):
    def test_missing_client(self) -> None:
        """ API should not run without a client. """

        api = SuiteSectionAPI()

        with self.assertRaises(Exception):
            api._list(1, 1)
