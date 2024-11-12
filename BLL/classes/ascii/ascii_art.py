import os
from sources.ascii_templates import ascii_templates 

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.symbol = "*"
        self.generated_art = ""
        self.alignment = "left"

    def get_console_width(self):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 80

    def user_input(self):
        return input("Enter text or phrase to convert to ASCII art: ")

    def choose_symbol(self):
        symbol = input("Enter a character to create ASCII art (eg. @, #, *): ").strip()
        return symbol if symbol else "*"

    def choose_alignment(self):
        while True:
            alignment = input("Select the alignment (left, center, right): ").strip().lower()
            if alignment in ["left", "center", "right"]:
                return alignment
            else:
                print("Wrong choice. Please select left, center or right.")

    def resize_ascii_art(self, art, width_scale, height_scale):
        lines = art.splitlines()
        scaled_art = []
        
        for line in lines:
            scaled_line = ''.join([char * width_scale for char in line])
            for _ in range(height_scale):
                scaled_art.append(scaled_line)
        
        return "\n".join(scaled_art)

    def preview_ascii_art(self, art):
        print("\nASCII art preview:\n")
        print(art)

    def generate_ascii_art(self, text, symbol, width_scale, height_scale, alignment):
        art_lines = [""] * 5
        for char in text.upper():
            if char in ascii_templates:
                for i in range(5):
                    line_with_symbol = ascii_templates[char][i].replace('*', symbol)
                    art_lines[i] += line_with_symbol + "  "

        console_width = self.get_console_width()
        
        if alignment == "center":
            aligned_art = [line.center(console_width) for line in art_lines]
        elif alignment == "right":
            aligned_art = [line.rjust(console_width) for line in art_lines]
        else:  # left
            aligned_art = [line.ljust(console_width) for line in art_lines]

        final_art = "\n".join(aligned_art)

        if width_scale > 1 or height_scale > 1:
            final_art = self.resize_ascii_art(final_art, width_scale, height_scale)

        return final_art

    def run(self):
        self.text = self.user_input()
        self.symbol = self.choose_symbol()
        self.alignment = self.choose_alignment()
        width_scale = int(input("Enter width scale (default 1): ") or 1)
        height_scale = int(input("Enter height scale (default 1): ") or 1)

        self.generated_art = self.generate_ascii_art(self.text, self.symbol, width_scale, height_scale, self.alignment)
        self.preview_ascii_art(self.generated_art)


