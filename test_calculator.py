import unittest
from calculator import *
#https://github.com/tzzing/lab10-CM-LG
#Partner 1: Christina Maribbay
#Partner 2: Lana Gerstenberger
class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 0), 2)
        self.assertNotEqual(add(2, 3), 4)


    def test_subtract(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(2, 0), 2)
        self.assertNotEqual(sub(4, 1), 4)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertEqual(log(1, 0), 0)
        self.assertEqual(log(1000,10), 3)
        self.assertNotEqual(log(2), 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-5, 0)

    
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