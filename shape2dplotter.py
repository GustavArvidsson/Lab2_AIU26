import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch
from matplotlib.patches import Rectangle as RectanglePatch


class Shape2dPlotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        self.ax.grid(True)


    def add_circle(self, circle):
        patch = CirclePatch((circle.x, circle.y), radius=circle.radius, fill=False)
        self.ax.add_patch(patch)

    def add_rectangle(self, rectangle):
        patch = RectanglePatch(
        (rectangle.x - rectangle.width / 2, rectangle.y - rectangle.height / 2), width=rectangle.width, height=rectangle.height, fill=False)
        self.ax.add_patch(patch)