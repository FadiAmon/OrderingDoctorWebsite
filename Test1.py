import unittest
import List_D


class Test_get_funch(unittest.TestCase):

    def test_get_first(self):
        self.assertIsNotNone(List_D.get__first_())

    def test_get_last(self):
        self.assertIsNotNone(List_D.get__last_())


if __name__ == '__main__':
    unittest.main()