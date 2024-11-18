from shared.functions import add_to_history, addition, division, get_history, memory_add, memory_clear, memory_recall, memory_store, modulus, multiplication, power, square_root, substraction
from shared.app_settings import decimal_places

class Calculator:
    def __init__(self):
        self.operations = {
            '+': addition,
            '-': substraction,
            '*': multiplication,
            '/': division,
            '^': power,
            'sqrt': square_root,
            '%': modulus
        }

    def get_operator(self):
        while True:
            try:
                operator = input("Enter operator (+, -, *, /, ^, sqrt, %): ").strip()
                if operator in self.operations:
                    return operator
                print("Invalid operator! Please enter a valid operator.")
            except Exception as e:
                print(f"Error: {e}")

    def get_operand(self, prompt):
        while True:
            try:
                operand = input(prompt).strip()
                if operand.upper() == 'MR':
                    value = memory_recall()
                    if value is None:
                        print("Memory is empty. Please enter a valid operand.")
                        continue
                    return value
                return float(operand)
            except ValueError:
                print("Invalid input! Please enter a float number or 'MR'.")
            except Exception as e:
                print(f"Error: {e}")

    def input(self):
        try:
            operator = self.get_operator()
            first_operand = self.get_operand("Enter the first operand or MR (Memory recall): ")

            if operator == 'sqrt':
              second_operand = None 
            else:
              second_operand = self.get_operand("Enter the second operand or MR (Memory recall): ")

            return first_operand, second_operand, operator
        except Exception as e:
            print(f"Error: {e}")
            return None, None, None

    def calculate(self, first_operand, second_operand, operator):
    
        if not isinstance(first_operand, (int,float)) or (second_operand is not None and not isinstance(second_operand, (int,float))):
            raise TypeError("All operands must be float numbers.")
        
        if operator == '/' and second_operand == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        try:
            operation = self.operations[operator]
            result = operation(first_operand, second_operand) if operator != 'sqrt' else operation(first_operand)
            return round(result, decimal_places) if result is not None else None

        except Exception as e:
            print(f"Error: {e}")
            return None

    def perform_memory_operation(self, result):
        try:
            memory_choice = input('Do you want to perform any memory operations ("MS" to store, "M+" to add, "MC" to clear)? Enter any other character if no : ').strip().upper()
            if memory_choice == 'MS':
                memory_store(result)
            elif memory_choice == 'M+':
                memory_add(result)
            elif memory_choice == 'MC':
                memory_clear()
        except Exception as e:
            print(f"Error: {e}")

    def show_history(self):
        try:
            show_history = input("Do you want to see the history of operations? (Enter 'yes' or any other character if no): ").strip().lower()
            if show_history == 'yes':
                for record in get_history():
                    print(record)
            else:
                print("History display canceled.")
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
         while True:
            first_operand, second_operand, operator = self.input()
            if operator is None:
                print("Invalid input. Please try again.")
                continue  

            result = None

            try:
                result = self.calculate(first_operand, second_operand, operator)
            except ZeroDivisionError as e:
                print(e) 
                continue  
            except TypeError as e:
                print(e)  
                continue 
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue 

            if result is not None:
                print(f"Result: {result}")
                add_to_history(f"{first_operand} {operator} {second_operand if second_operand is not None else ''} = {result}")
                self.perform_memory_operation(result)

                self.show_history()

            repeat = input("Do you want to perform another calculation? (Enter 'yes' or any other character if no): ").strip().lower()
            if repeat != 'yes':
                break


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()