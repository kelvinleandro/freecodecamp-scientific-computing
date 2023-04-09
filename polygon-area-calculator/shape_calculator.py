class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height    

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        pic = ''
        for _ in range(self.height):
            pic += '*' * self.width + '\n'

        return pic

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __repr__(self) -> str:
        return f"Square(side={self.height})"

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    # Override
    def set_width(self, side):
        self.width = side
        self.height = side

    # Override
    def set_height(self, side):
        self.width = side
        self.height = side

