import unittest
import app


class Test_get_funch(unittest.TestCase):

    def test_get_first(self):
        self.assertIsNotNone(app.calc_distance_of_two_points('Dimona','Hadera'))

if __name__ == '__main__':
    unittest.main()