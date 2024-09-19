import math


def addition (num1, num2):
 result = num1 + num2
 return result 

def substraction (num1, num2):
   result = num1 - num2
   return result 

def multiplication (num1, num2):
   result = num1 * num2
   return result 

def division (num1, num2):
   while num2 == 0:
        print('You cannot divide by zero')
        num2 = float(input('Enter another second number: '))

   result = num1 / num2
   return result

def power(num1, num2):
    result = num1 ** num2
    return result

def square_root(num):
    if num < 0:
        return 'It is impossible to take the root of a negative number.'
    result = math.sqrt(num)
    return result

def modulus(num1, num2):
    result = num1 % num2
    return result