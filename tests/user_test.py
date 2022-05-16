import unittest

from testlodge import UserJSON


class TestUser(unittest.TestCase):
    """Test User"""

    def test_simple(self):

        user_dict: UserJSON = dict(
            id=123456,
            firstname='First',
            lastname='Last',
            email='user@email.com',
            created_at="2022-01-01T20:30:40.123456Z",
            updated_at="2022-05-16T01:08:41.493190Z",
        )

        # This operation is not supported at this time.
        # self.assertTrue(isinstance(user_dict, UserJSON))
