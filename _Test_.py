import unittest
import Project

class MyTestCase(unittest.TestCase):
    def test(self):
        Project.email = 'tot@gmail.com'
        self.assertEqual(Project.get_email(), 'tot@gmail.com')
        self.assertNotEqual(Project.get_email(), 'tot1@gmail.com')
        self.assertIsNotNone(Project.get_email())

    def test1(self):
        Project.email = 'tot@gmail.com'
        self.assertEqual(Project.get_first(), 'tot')
        self.assertNotEqual(Project.get_first(), 'tot1')
        self.assertIsNotNone(Project.get_first())

    def test2(self):
        Project.email = 'tot@gmail.com'
        self.assertEqual(Project.get_last(), 'qeq')
        self.assertNotEqual(Project.get_last(), 'qeq1')
        self.assertIsNotNone(Project.get_last())

    def test3(self):
        Project.email = 'tot@gmail.com'
        self.assertEqual(Project.get_pass(), '12345')
        self.assertNotEqual(Project.get_pass(), '123456')
        self.assertIsNotNone(Project.get_pass())

    def test4(self):
        Project.email = 'tot@gmail.com'
        self.assertEqual(Project.get_d_p_a(), 'Doctor')
        self.assertNotEqual(Project.get_d_p_a(), 'test')
        self.assertIsNotNone(Project.get_d_p_a())

    def test5(self):
        Project.email = 'qoq@gmail.com'
        self.assertEqual(Project._get__first_(), 'ror')
        self.assertNotEqual(Project._get__first_(), 'ror1')
        self.assertIsNotNone(Project._get__first_())

    def test6(self):
        Project.email = 'qoq@gmail.com'
        self.assertEqual(Project._get__last_(), 'qoq')
        self.assertNotEqual(Project._get__last_(), 'qoq1')
        self.assertIsNotNone(Project._get__last_())

    def test7(self):
        self.assertEqual(Project.get_d_p_a__('tot', 'qeq', 'tot@gmail.com'), 'Doctor')
        self.assertNotEqual(Project.get_d_p_a__('tot', 'qeq', 'tot@gmail.com'), 'test')
        self.assertIsNotNone(Project.get_d_p_a__('tot', 'qeq', 'tot@gmail.com'))

    def test8(self):
        self.assertEqual(Project.check_count_('tot', 'qeq', 'tot@gmail.com'), 0)
        self.assertNotEqual(Project.check_count_('tot', 'qeq', 'tot@gmail.com'), 9)
        self.assertIsNotNone(Project.check_count_('tot', 'qeq', 'tot@gmail.com'))

    def test9(self):
        app = Project.Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test10(self):
        Project.email = 'ward@gmail.com'
        self.assertEqual(Project.get_first_(), 'ward')
        self.assertNotEqual(Project.get_first_(), 'ward1')
        self.assertIsNotNone(Project.get_first_())

    def test11(self):
        Project.email = 'ward@gmail.com'
        self.assertEqual(Project.get_last_(), 'kadan')
        self.assertNotEqual(Project.get_last_(), 'kadan1')
        self.assertIsNotNone(Project.get_last_())

if __name__ == '__main__':
    unittest.main()
