from abc import ABC, abstractmethod

from BLL import functions


class Operation(ABC):
    @abstractmethod
    def execute(self, first_operand, second_operand):
        pass  

class Addition(Operation):
    def execute(self, first_operand, second_operand):
        return functions.addition(first_operand, second_operand)
    
class Subtraction(Operation):
    def execute(self, first_operand, second_operand):
        return functions.substraction(first_operand, second_operand)

class Multiplication(Operation):
    def execute(self, first_operand, second_operand):
        return functions.multiplication(first_operand, second_operand)

class Division(Operation):
    def execute(self, first_operand, second_operand):
        return functions.division(first_operand, second_operand)

class Power(Operation):
    def execute(self, first_operand, second_operand):
        return functions.power(first_operand, second_operand)

class SquareRoot(Operation):
    def execute(self, first_operand, second_operand=None):
        return functions.square_root(first_operand)

class Modulus(Operation):
    def execute(self, first_operand, second_operand):
        return functions.modulus(first_operand, second_operand)