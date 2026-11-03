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