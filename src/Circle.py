import math
import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return 5

    def get_perimeter(self):
        return 2 * math.pi * self.radius
