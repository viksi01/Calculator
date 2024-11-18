import os, sys
from labs.lab2.calculator import Calculator
from shared.app_settings import set_decimal_places
from labs.lab4.ascii_art import ASCIIArtGenerator
from labs.lab3.ascii_art_pyfiglet import AsciiArtPyfiglet
from labs.lab5.threeD_art import ThreeDArtGenerator



class Menu:
    def __init__(self):
        self.calculator = Calculator()
        self.ascii_art_generator = ASCIIArtGenerator()
        self.ascii_art_pyfiglet = AsciiArtPyfiglet()
        self.threeD_art_generator = ThreeDArtGenerator()

    def display(self):
        while True:
            print("Menu")
            print("1. Calculator")
            print("2. Ascii art generator with pyfiglet")
            print("3. Ascii art generator")
            print("4. ThreeD art generator")
            print("5. Settings")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                self.calculator.run()  
            elif choice == '2':
                self.ascii_art_pyfiglet.run()
            elif choice == '3':
                self.ascii_art_generator.run() 
            elif choice == '4':
                self.threeD_art_generator.run()
            elif choice == '5':
                set_decimal_places()
            elif choice == '6':
                break
            else:
                print("Invalid choice, please select a number between 1 and 5.")