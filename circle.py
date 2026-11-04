import math
class Circle:
    def __init__(self, radius: float, x: float = 0, y: float = 0):
        self.radius = radius
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return math.pi * self.radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def translate(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def __eq__(self, other):
            if isinstance(other, Circle):
                return (self.radius == other.radius)
            return False