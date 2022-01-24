# Работа с файлами
# Открытие файла
# open(file[, mode='r', encoding='utf-8', ...])

file = open('folder/my_file.txt', encoding='utf-8')
print(file.read(4))
print(file.read(4))
print(file.read(4))
file.seek(0)  # перемещаем курсор в начало файла
print(file.read(4))
print(file.tell()) # возвращает позицию курсора



file.close()

file = open('folder/my_file.txt', encoding='utf-8')
print(file.readline(), end='')
print(file.readline())

file.seek(0)
for i in file:
    print(i, end='')

file.seek(0)
s = file.readlines()
print(s)
file.close()