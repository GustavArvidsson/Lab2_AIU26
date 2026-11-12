from .shape3d import Shape3d, type_error, number_error
import math

class Sphere(Shape3d):
    def __init__(self, radius: float, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y, z)
        type_error(radius, "radius")
        number_error(radius, "radius")
        self.radius = radius

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def __str__(self):
        return f"Sphere has radius = {self.radius} and position: x = {self.x}, y = {self.y}, z = {self.z}"

    def __repr__(self):
        return f"Sphere:(radius:{self.radius}, x:{self.x}, y:{self.y}, z:{self.z})"