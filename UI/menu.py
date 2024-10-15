from BLL.classes.calculator import Calculator
from BLL.settings import set_decimal_places

class Menu:
    def __init__(self):
        self.calculator = Calculator()

    def display(self):
        while True:
            print("Menu")
            print("1. Calculator")
            print("2. Settings")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ").strip()

            if choice == '1':
                self.calculator.run()  
            elif choice == '2':
                set_decimal_places() 
            elif choice == '3':
                break
            else:
                print("Invalid choice, please select a number between 1 and 3.")