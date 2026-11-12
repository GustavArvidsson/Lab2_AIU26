from .circle import Circle
from .rectangle import Rectangle
from .cube import Cube
from .sphere import Sphere
from .shape import Shape
from .shape3d import Shape3d
from .shape2dplotter import Shape2dPlotter

__all__ = ["Circle", "Rectangle", "Cube", "Sphere", "Shape", "Shape3d", "Shape2dPlotter"]


def main() -> None:
    """Entry point for the project command."""
    print("Hello from lab2-aiu26!")
