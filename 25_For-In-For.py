for i in range(1, 4):
    for j in range(1, 6):
        print(f'i = {i}, j = {j}', end=' ')
    print()

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
c = []
for row in a:
    for item in row:
        print(item, end=' ')
    print()

for i, row in enumerate(a):
    r = []
    for j, item in enumerate(row):
        r.append(item + b[i][j])
    c.append(r)

print(c)

t = ["Скажи мне, как тебя  зовут?", "Как   дела?", "Как  настроение?"]
for i, line in enumerate(t):
    while line.count("  "):
        line = line.replace("  ", " ")
    t[i] = line

print(t)

print("..................... Задача .........................")

M, N = list(map(int, input("Введите размерность матрицы: ").split()))
zeros = []
for i in range(M):
    zeros.append([0] * N)
print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1
print(zeros)

print("..................... Задача 2.........................")

t = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def matrix(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='\t')
        print()


matrix(t)
for i in range(len(t)):
    for j in range(i + 1, len(t)):
        t[i][j], t[j][i] = t[j][i], t[i][j]
matrix(t)
