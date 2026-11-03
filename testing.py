from rectangle import Rectangle
from circle import Circle

rect1 = Rectangle(5, 10)
circ1 = Circle(3)

print (f"Rectangle perimeter: {rect1.perimeter}")
print (f"Rectangle area: {rect1.area}")
print(f"Rectangle position: ({rect1.x}, {rect1.y})")

print (f"Circle perimeter: {circ1.perimeter}")
print (f"Circle area: {circ1.area}")

rect1.translate(2,5)
print(f"Rectangle new position: ({rect1.x}, {rect1.y})")

rect1.translate(6,-2)
print(f"Rectangle new position: ({rect1.x}, {rect1.y})")