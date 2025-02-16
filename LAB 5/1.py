class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
        else:
            self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    @staticmethod
    def input_matrix():
        rows = int(input("Введіть кількість рядків: "))
        cols = int(input("Введіть кількість стовпців: "))
        print("Введіть елементи матриці по рядках:")
        data = []
        for i in range(rows):
            row = list(map(int, input().split()))
            data.append(row)
        return Matrix(rows, cols, data)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці повинні мати однаковий розмір!")
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матриці повинні мати однаковий розмір!")
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(self.rows, self.cols, result_data)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці!")
        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(self.rows, other.cols, result_data)

# Введення двох матриць
print("Введення першої матриці:")
matrix1 = Matrix.input_matrix()

print("Введення другої матриці:")
matrix2 = Matrix.input_matrix()

# Вивід результатів операцій
print("\nСума матриць:")
print(matrix1 + matrix2)

print("\nРізниця матриць:")
print(matrix1 - matrix2)

print("\nДобуток матриць:")
print(matrix1 * matrix2)
