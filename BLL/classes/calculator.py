from BLL.classes.history import History
from BLL.classes.memory import Memory
from BLL.classes.operation import Addition, Division, Modulus, Multiplication, Power, SquareRoot, Subtraction
from BLL.settings import decimal_places


class Calculator:
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Power(),
            'sqrt': SquareRoot(),
            '%': Modulus()
        }

    def get_operator(self):
        operator = input("Enter operator (+, -, *, /, ^, sqrt, %): ").strip()
        if operator not in self.operations:
            raise ValueError("Invalid operator!")
        return operator

    def get_operand(self, prompt):
        operand = input(prompt).strip()
        if operand == 'MR':
            return self.memory.recall()
        return float(operand)

    def input(self):
        operator = self.get_operator()
        
        first_operand = self.get_operand("Enter the first operand or MR (Memory recall): ")
        
        if operator != 'sqrt':
            second_operand = self.get_operand("Enter the second operand or MR (Memory recall): ")
        else:
            second_operand = None
        
        return first_operand, second_operand, operator

    def calculate(self, first_operand, second_operand, operator):
        operation = self.operations[operator]
        try:
            result = operation.execute(first_operand, second_operand)
            return round(result, decimal_places)
        except Exception as e:
            print(f"Error: {e}")
            return None

    def perform_memory_operation(self, result):
        memory_choice = input('Do you want to perform any memory operations ("MS" to store in memory, "M+" to add to memory, "MC" to clean memory)? ').strip().upper()
        if memory_choice == 'MS':
            self.memory.store(result)
        elif memory_choice == 'M+':
            self.memory.add(result)
        elif memory_choice == 'MC':
            self.memory.clear()

    def show_history(self):
        show_history = input("Do you want to see the history of operations? (y/n): ").strip().lower()
        if show_history == 'y':
            self.history.show()

    def run(self):
        while True:
            first_operand, second_operand, operator = self.input()
            if operator is None:
                continue
            result = self.calculate(first_operand, second_operand, operator)

            if result is not None:
                print(f"Result: {result}")
                self.history.add(f'{first_operand} {operator} {second_operand if operator != "sqrt" else ""} = {result}')

                self.perform_memory_operation(result)

                self.show_history()

            repeat = input("Do you want to perform another calculation? (y/n):  ").strip().lower()
            if repeat == 'n':
                break