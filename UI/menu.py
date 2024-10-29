from bll.classes.calculator import Calculator
from bll.settings import set_decimal_places
from ascii import run_ascii

class Menu:
    def __init__(self):
        self.calculator = Calculator()

    def display(self):
        while True:
            print("Menu")
            print("1. Calculator")
            print("2. Settings")
            print("3. Ascii art generator")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ").strip()

            if choice == '1':
                self.calculator.run()  
            elif choice == '2':
                set_decimal_places() 
            elif choice == '3':
                run_ascii() 
            elif choice == '4':
                break
            else:
                print("Invalid choice, please select a number between 1 and 4.")