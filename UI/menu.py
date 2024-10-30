from bll.classes.calculator import Calculator
from bll.settings import set_decimal_places
from ascii.ascii_art import ASCIIArtGenerator
from ascii.ascii_art_pyfiglet import run_ascii

class Menu:
    def __init__(self):
        self.calculator = Calculator()
        self.ascii_art_generator = ASCIIArtGenerator()

    def display(self):
        while True:
            print("Menu")
            print("1. Calculator")
            print("2. Ascii art generator with pyfiglet")
            print("3. Ascii art generator")
            print("4. Settings")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                self.calculator.run()  
            elif choice == '2':
                run_ascii() 
            elif choice == '3':
                self.ascii_art_generator.run() 
            elif choice == '4':
                set_decimal_places()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please select a number between 1 and 5.")