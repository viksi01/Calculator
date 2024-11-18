import random
import string
import unittest
from labs.lab2.calculator import Calculator
from shared.app_settings import decimal_places


class AdditionUnitTests(unittest.TestCase):
    def setUp(self):
        self.operator = '+'
    
    def test_addition_positive_numbers(self):
        test_first_operand = random.uniform(1, 100)
        test_second_operand = random.uniform(1, 100)
        expected = test_first_operand + test_second_operand
        calc = Calculator()
        result = calc.calculate(test_first_operand, test_second_operand, self.operator)
        self.assertAlmostEqual(expected, result, places = decimal_places)
    
    def test_addition_negative_numbers(self):
        test_first_operand = random.uniform(-100, -1)
        test_second_operand = random.uniform(-100, -1)
        expected = test_first_operand + test_second_operand
        calc = Calculator()
        result = calc.calculate(test_first_operand, test_second_operand, self.operator)
        self.assertAlmostEqual(expected, result, places = decimal_places)

    def test_addition_wrong_input(self):
        test_first_operand = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        test_second_operand = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.calculate(test_first_operand, test_second_operand, self.operator)


if __name__ == '__main__':
    unittest.main()



