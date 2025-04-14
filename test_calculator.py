# https://github.com/tzzing/lab10-CM-LG
# Partner 1: Christina Maribbay
# Partner 2: Lana Gerstenberger

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 0), 2)
        self.assertNotEqual(add(2, 3), 4)


    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(2, 0), 2)
        self.assertNotEqual(subtract(4, 1), 4)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 1), 0)
        self.assertAlmostEqual(logarithm(1000,10), 0.3, places = 1)
        self.assertNotEqual(logarithm(2, 4), 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(2,-5)

    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()