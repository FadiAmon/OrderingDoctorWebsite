import unittest
import Change_specialty


class Test_get_funch(unittest.TestCase):

    def test_get_first(self):
        self.assertIsNotNone(Change_specialty.get_first())

    def test_get_last(self):
        self.assertIsNotNone(Change_specialty.get_last())


if __name__ == '__main__':
    unittest.main()