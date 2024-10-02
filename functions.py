import math

def check_floats(*operands):
    for operand in operands:
        if not isinstance(operand, float):
            raise ValueError("All operands must be float numbers.")
        
def addition(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return first_operand + second_operand

def substraction(first_operand, second_operand):
    check_floats(first_operand, second_operand) 
    return first_operand - second_operand

def multiplication (first_operand, second_operand):
    check_floats(first_operand, second_operand) 
    return first_operand * second_operand

def division(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    while second_operand == 0:
        print('You cannot divide by zero')
        second_operand = float(input('Enter another second number: '))

    return first_operand / second_operand

def power(first_operand, second_operand):
    check_floats(first_operand, second_operand) 
    return pow(first_operand, second_operand)

def square_root(operand):
    check_floats(operand) 
    if operand < 0:
        return 'It is impossible to take the root of a negative number.'
    return math.sqrt(operand)

def modulus(first_operand, second_operand):
    check_floats(first_operand, second_operand) 
    return first_operand % second_operand