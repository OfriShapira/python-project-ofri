import unittest


class CarTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case
        :return: None
        """
        self.t = Car()

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
