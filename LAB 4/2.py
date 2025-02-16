class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
   
    x1, y1 = map(int, input("Введіть координати першого вектора (x y): ").split())
    x2, y2 = map(int, input("Введіть координати другого вектора (x y): ").split())

    vector1 = Vector(x1, y1)
    vector2 = Vector(x2, y2)

    print(f"Сума векторів: {vector1 + vector2}")
    print(f"Різниця векторів: {vector1 - vector2}")
