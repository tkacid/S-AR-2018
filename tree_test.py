import unittest
from tree import make_flora, check_input
import config


class TestTree(unittest.TestCase):
    """
    basic test class for tree.py
    """

    def test_make_flora(self):

        # Execute Test
        res, result = make_flora(config.testvalue)
        # Check to see if we received the returned result
        self.assertEqual(result, config.testvalue)

    def test_check_input(self):

        # Test input of check input
        res = check_input(config.test_low, config.test_high, config.testvalue)

        # Review result
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
