import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(4, 1), 3)
        self.assertEqual(subtract(0, 2), -2)
        self.assertEqual(subtract(-1, -1), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)

    # def test_divide(self): # 3 assertions
    #     fill in code
    def test_divide(self):
        self.assertEqual(div(2, 10), 5)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 16), 4)
        self.assertEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 3)

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 0)

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code
    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()