# file  = open("folder/test.txt", "w+")
# file.write("Hello Nikolay Nikolayenko!\n")
# file.close()

# то же самое

try:
    with open("folder/testWriteFile.txt", "w") as file:
        file.write("Hello Nikolay Nikolayenko!\n")
        file.write("Hello Nikolay Nikolayenko!\n")
        file.write("Hello Nikolay Nikolayenko!\n")
except:
    print("Ошибка при открытии файла")

# append append
# добавляет в файл новый текст

try:
    with open("folder/testWriteFile.txt", "a") as file:
        file.write("Hello Nikolay Nikolayenko!\n")
        file.write("Hello Nikolay Nikolayenko!\n")
        file.write("Hello Nikolay Nikolayenko!\n")
except:
    print("Ошибка при открытии файла")

try:
    with open("folder/testWriteFile.txt", "a+") as file:
        # a+ открывает файл на чтение и запись и перемещается в конец файла
        file.seek(0)
        file.writelines(["Привет",", ", "Как дела?\n"])
        s = file.read()
        print(s)
except:
    print("Ошибка при открытии файла")

# binary file

books = [
    ("Война и мир", "Лев Толстой", 1869, "Русский"),
    ("Отцы и дети", "И. Тургенев", 1862, "Русский"),
    ("Чайка", "А. Чехов", 1813, "Русский"),
    ("Преступление и наказание", "Ф. М. Достоевский", 1866, "Русский"),
]

import pickle

file = open("folder/testWriteBineryFile.bin", "wb")
pickle.dump(books, file)
file.close()

file = open("folder/testWriteBineryFile.bin", "rb")
bs = pickle.load(file)
print(bs)
file.close()

book1 = ("Война и мир", "Лев Толстой", 1869, "Русский")
book2 = ("Отцы и дети", "И. Тургенев", 1862, "Русский")
book3 = ("Чайка", "А. Чехов", 1813, "Русский")

try:
    with open("folder/testWriteBineryFile.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
except:
    print("Ошибка при открытии файла")

try:
    with open("folder/testWriteBineryFile.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        print(b1)
        print(b2)
        print(b3)
except:
    print("Ошибка при открытии файла")