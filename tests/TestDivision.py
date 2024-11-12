import random
import string
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bll.classes.calculator.calculator import Calculator
from app_settings import decimal_places


class DivisionUnitTests(unittest.TestCase):
    def setUp(self):
        self.operator = '/'
    
    def test_division_positive_numbers(self):
        test_first_operand = random.uniform(1, 100)
        test_second_operand = random.uniform(1, 100)
        expected = test_first_operand / test_second_operand
        calc = Calculator()
        result = calc.calculate(test_first_operand, test_second_operand, self.operator)
        self.assertAlmostEqual(expected, result, places = decimal_places)
    
    def test_division_negative_numbers(self):
        test_first_operand = random.uniform(-100, -1)
        test_second_operand = random.uniform(-100, -1)
        expected = test_first_operand / test_second_operand
        calc = Calculator()
        result = calc.calculate(test_first_operand, test_second_operand, self.operator)
        self.assertAlmostEqual(expected, result, places = decimal_places)

    def test_division_by_zero(self):
        test_first_operand = random.uniform(1, 100)
        test_second_operand = 0
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.calculate(test_first_operand, test_second_operand, self.operator)


if __name__ == '__main__':
    unittest.main()



