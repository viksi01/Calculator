import os
import pyfiglet
from termcolor import colored


class AsciiArtPyfiglet:
    def __init__(self):
        self.fonts = ['slant', '3-d', '5lineoblique', 'standard', 'big', 'block', 'bubble', 'digital', 'isometric1',
                      'banner']
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def user_input(self):
        return input("Enter the text to convert to ASCII art: ")

    def choose_font(self):
        print("Available fonts:")
        for i, font in enumerate(self.fonts):
            print(f"{i + 1}. {font}")

        try:
            font_choice = int(input("Choose a font by number: "))
            return self.fonts[font_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Defaulting to 'slant'.")
            return 'slant'

    def choose_color(self):
        print("Available colors:")
        for i, color in enumerate(self.colors):
            print(f"{i + 1}. {color}")

        try:
            color_choice = int(input("Choose a color by number: "))
            return self.colors[color_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Defaulting to 'white'.")
            return 'white'

    def choose_symbols(self):
        custom_char = input("Enter the character you'd like to use instead of default ASCII characters (optional): ")
        return custom_char if custom_char else None

    def generate_ascii_art(self, text, font, custom_char=None):
        ascii_art = pyfiglet.Figlet(font=font)
        art = ascii_art.renderText(text)

        if custom_char:
            for old_char in set(art):
                if old_char not in ['\n', ' ']:
                    art = art.replace(old_char, custom_char)

        return art

    def display_ascii_art(self, art, color):
        print(colored(art, color))

    def save_to_file(self, art, filename="ascii_art"):
        filename += '.txt'
        while os.path.exists(filename):
            choice = input(
                f"The file '{filename}' already exists. Overwrite it? (Enter 'yes' or any character if no): ").strip().lower()
            if choice == 'yes':
                break
            else:
                filename = input("Please enter a new filename: ").strip()

        with open(filename, 'w') as file:
            file.write(art)
        print(f"ASCII art saved to {filename}")

    def resize_ascii_art(self, art, width_scale, height_scale):
        lines = art.splitlines()
        scaled_art = []

        for line in lines:
            scaled_line = ''.join([char * width_scale for char in line])
            scaled_art.append(scaled_line)

        final_art = []
        for line in scaled_art:
            for _ in range(height_scale):
                final_art.append(line)

        return "\n".join(final_art)

    def preview_art(self, art, color):
        print("\nPreview of your ASCII art:")
        self.display_ascii_art(art, color)

    def run(self):
        text = self.user_input()
        font = self.choose_font()
        color = self.choose_color()
        custom_char = self.choose_symbols()

        ascii_art = self.generate_ascii_art(text, font, custom_char)

        try:
            width_scale = int(input("Enter width scale factor (1 for normal, 2 for double width): "))
            height_scale = int(input("Enter height scale factor (1 for normal, 2 for double height): "))

            if width_scale not in [1, 2]:
                raise ValueError("Invalid choice for width scale!")
            if height_scale not in [1, 2]:
                raise ValueError("Invalid choice for height scale!")
        except ValueError as e:
            print(f"Error: {e}")
            return

        resized_art = self.resize_ascii_art(ascii_art, width_scale, height_scale)
        self.preview_art(resized_art, color)

        save_choice = input(
            "Do you want to save the ASCII art to a file? (Enter 'yes' or any character if no): ").strip().lower()
        if save_choice == 'yes':
            filename = input("Enter filename: ")
            self.save_to_file(resized_art, filename)

