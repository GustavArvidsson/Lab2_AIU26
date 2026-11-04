class Rectangle:
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy
        print(f"new position: ({self.x}, {self.y})")

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width == other.width and
                    self.height == other.height)
        return False 

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"