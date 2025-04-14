# https://github.com/tzzing/lab10-CM-LG
# Partner 1: Christina Maribbay
# Partner 2: Lana Gerstenberger

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 4), 4)
        self.assertEqual(mul(-5, 10), -50)
        self.assertEqual(mul(-8, -9), 72)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4 ), 2)
        self.assertEqual(div(-3, -9), 3)
        self.assertEqual(div(-6, 24), -4)

    ###########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        self.assertRaises(ValueError, logarithim(0,5))



    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(5, 6), 7.8, places = 1)
        self.assertAlmostEqual(hypotenuse(-9, 7), 11.4, places =1)
        self.assertAlmostEqual(hypotenuse(-4,-5), 6.4, places = 1)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertRaises(ValueError, square_root(-4))
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(7), 2.6)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()