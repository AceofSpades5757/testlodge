import unittest

from testlodge.api.suite_section import SuiteSectionAPI


class TestAPI(unittest.TestCase):
    def test_simple(self) -> None:
        _ = SuiteSectionAPI('dummy-client')
