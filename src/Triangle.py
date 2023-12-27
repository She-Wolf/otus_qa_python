import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a + side_b < side_c or side_a + side_c < side_b or side_c + side_b < side_a:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"

    @property
    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c