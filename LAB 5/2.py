import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

class Triangle:
    def __init__(self, point1, point2, point3):
        self.segment1 = Segment(point1, point2)
        self.segment2 = Segment(point2, point3)
        self.segment3 = Segment(point3, point1)

    def perimeter(self):
        return self.segment1.length() + self.segment2.length() + self.segment3.length()

def get_point_input(name):
    x = float(input(f"Введіть координату x для точки {name}: "))
    y = float(input(f"Введіть координату y для точки {name}: "))
    return Point(x, y)

if __name__ == "__main__":
    print("=== Обчислення довжини відрізка ===")
    A = get_point_input("A")
    B = get_point_input("B")
    segment = Segment(A, B)
    print(f"Довжина відрізка AB: {segment.length()}")

    print("\n=== Обчислення периметра трикутника ===")
    C = get_point_input("C")
    triangle = Triangle(A, B, C)
    print(f"Периметр трикутника ABC: {triangle.perimeter()}")
