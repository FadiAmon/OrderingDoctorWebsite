import unittest
import orders__

class MyTestCase(unittest.TestCase):
    def test_something(self):
        orders__.email = 'tot@gmail.com'
        self.assertEqual(orders__.get_email(), 'tot@gmail.com')
        self.assertNotEqual(orders__.get_email(), 'tot1@gmail.com')
        self.assertIsNotNone(orders__.get_email())


if __name__ == '__main__':
    unittest.main()
