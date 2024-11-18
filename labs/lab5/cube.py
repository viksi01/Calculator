from labs.lab5.base_figure import BaseFigure

class Cube(BaseFigure):
    def __init__(self, side_a: int, horizontal_shift: int = 10, vertical_shift: int = 0):
        super().__init__(side_a)
        self.side_a = side_a
        self.horizontal_shift = horizontal_shift
        self.vertical_shift = vertical_shift

    def get_two_d_art(self):
        result = "\n" * self.vertical_shift  
        for side_a_pixel in range(self.side_a):
            result += " " * self.horizontal_shift
            result += "* "
            for side_b_pixel in range(self.side_a - 2):
                if side_a_pixel == 0 or side_a_pixel == self.side_a - 1:
                    result += "* "
                else:
                    result += "  "
            result += "*\n"
        return result

    def get_three_d_art(self):
        result = "\n" * self.vertical_shift  
        art_size = int(self.side_a + self.side_a / 2)
        side_side_size = int(self.side_a / 1.5)

        space_counter = 0
        for x in range(art_size):
            result += " " * self.horizontal_shift  
            
            if x == 0:
                result += "* " * self.side_a 
            elif x < side_side_size:
                result += "* " + space_counter * "  " + "* "
                space_counter += 1
            elif side_side_size <= x <= art_size - side_side_size:
                result += "* " + (side_side_size - 2) * "  " + "* "
                space_counter = 1
            elif x < art_size - 1:
                result += space_counter * "  " + "* " + (art_size - x - 2) * "  " + "* "
                space_counter += 1
            else:
                result += space_counter * "  " + "* "

            for y in range(self.side_a - 2):
                if x == 0 or x == side_side_size - 1 or x == art_size - 1:
                    result += "* "
                else:
                    result += "  "

            result += "*\n"

        return result
