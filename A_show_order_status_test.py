import unittest
import A_show_order_status

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(A_show_order_status.ret_result(), 'tot@gmail.com')
        self.assertNotEqual(A_show_order_status.ret_result(), 'tot1@gmail.com')
        self.assertIsNotNone(A_show_order_status.ret_result())

if __name__ == '__main__':
    unittest.main()
