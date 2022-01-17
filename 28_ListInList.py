a = [(i, j) for i in range(3) for j in range(4)]
print(a)

a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]
print(a)

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
a = [x
     for row in matrix
     for x in row
     ]
print(a)
a = [x for row in matrix for x in row]
print(a)

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

print("....................................................")

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[x ** 2 for x in row] for row in A] # Пример использования цикла внутри цикла
print(A)

AA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [x ** 2
     for row in AA
     for x in row
     ]
print(A)

def print_matrix(matrix):
    for row in matrix:
        print(*row)

#Транспонирование матрицы
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix(A)
A = [[row[i] for row in A] for i in range(len(A[0]))]
print_matrix(A)
