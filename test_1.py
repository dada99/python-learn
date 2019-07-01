import unittest

from functions import func2


class TestSum(unittest.TestCase):
    def test_double_func(self):
        """
        Test that it can double the input
        """
        data = 2
        result = func2(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
