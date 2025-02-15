rows = int(input("Введіть кількість рядків матриці: "))
cols = int(input("Введіть кількість стовпців матриці: "))
matrix = []
for i in range(rows):
    matrix.append(list(map(int, input().split())))

max_val, min_val = float('-inf'), float('inf')
max_pos, min_pos = (0, 0), (0, 0)
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_val:
            max_val, max_pos = matrix[i][j], (i, j)
        if matrix[i][j] < min_val:
            min_val, min_pos = matrix[i][j], (i, j)

print(f"Максимальний елемент {max_val} знаходиться у рядку {max_pos[0]+1}, стовпці {max_pos[1]+1}")
print(f"Мінімальний елемент {min_val} знаходиться у рядку {min_pos[0]+1}, стовпці {min_pos[1]+1}")
