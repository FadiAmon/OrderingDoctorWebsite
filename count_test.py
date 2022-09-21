import unittest

import A_show_count


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertNotEqual(A_show_count.ret_result(), "[('tot', 'tot@gmail.com', 0)]")
        self.assertNotEqual(A_show_count.ret_result(), 'test')
        self.assertIsNotNone(A_show_count.ret_result())


if __name__ == '__main__':
    unittest.main()
