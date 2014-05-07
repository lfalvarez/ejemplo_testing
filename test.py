import unittest
from Math import Math


class MathTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_class_exists(self):
        self.assertTrue(Math)

    def test_sum(self):
        self.assertEqual(Math.sum(2,2),4)

    def test_div(self):
        self.assertEqual(Math.div(4,2),2)

    def test_div_zero(self):
        x=Math()
        self.assertEqual(x.div(4,0),Math.INFINITE)

    def test_div_zero_zero(self):
        x=Math()
        self.assertEqual(x.div(0,0),Math.UNDEFINED)

    def test_div_return_zero(self):
        x=Math()
        self.assertEqual(x.div(0,4),0)

if __name__ == '__main__':
        unittest.main()
