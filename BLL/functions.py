import math

def check_floats(*operands):
    for operand in operands:
        if not isinstance(operand, float):
            raise ValueError("All operands must be float numbers.")

# operation functions
def addition(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return first_operand + second_operand

def substraction(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return first_operand - second_operand

def multiplication(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return first_operand * second_operand

def division(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    while second_operand == 0:
        print("You cannot divide by zero")
        second_operand = float(input("Enter another second number: "))
    return first_operand / second_operand

def power(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return pow(first_operand, second_operand)

def square_root(operand):
    check_floats(operand)
    if operand < 0:
        return "It is impossible to take the root of a negative number."
    return math.sqrt(operand)

def modulus(first_operand, second_operand):
    check_floats(first_operand, second_operand)
    return first_operand % second_operand

# memory functions
memory = None

def memory_store(value):
    global memory
    memory = value

def memory_recall():
    return memory

def memory_clear():
    global memory
    memory = None

def memory_add(value):
    global memory
    if memory is None:
        memory = value
    else:
        memory += value

# history functions
history = []

def add_to_history(record):
    history.append(record)

def get_history():
    return history

def clear_history():
    history.clear()
