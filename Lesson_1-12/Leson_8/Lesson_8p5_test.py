import unittest
from Lesson_8p5_main import *


class My_Test(unittest.TestCase):

    def test_args(self):
        self.assertEqual(adder(2, 2), 4)
        self.assertEqual(adder(3.5, 3.5), 7)
        self.assertEqual(adder(3, 4, 5), 12)


    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)


    def test_mixed(self):
        self.assertEqual(adder(1, c=2), 3)


    def test_diff(self):
        x = 10
        y =0
        self.assertEqual(adder(0, -5, y, a=x), 3)

    def test_wrong_dt(self):
        self.assertEqual(adder("5", "abc", 10), 15)
if __name__ == "__main__":
    unittest.main()