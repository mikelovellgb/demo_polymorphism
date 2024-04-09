from common.Shapes import Square, Circle, Triangle, Mystery

shapes = [Triangle(), Square(), Circle(), Mystery()]

for shape in shapes:
    print(f"The {shape.name()} has {shape.corners()} corners and {shape.sides()} sides.")