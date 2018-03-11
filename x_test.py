import unittest
from xpattern import make_da_x, check_input
import config


class TestTree(unittest.TestCase):
    """
    basic test class for tree.py
    """

    def test_make_da_x(self):

        # Execute Test
        res = make_da_x(config.x_testvalue)
        # Check to see if we received the returned result
        self.assertEqual(res, config.x_testvalue)

    def test_check_input(self):

        # Test input of check input
        res = check_input(config.x_test_low, config.x_test_high, config.x_testvalue)

        # Review result
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
