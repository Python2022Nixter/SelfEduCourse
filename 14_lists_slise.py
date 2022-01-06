# list(start:stop)
lst = ["Tel Aviv", "Tokio", "New York", "Kiev", "Montreal"]
print(lst)

lst2 = lst[1:4]
print(lst2)

lst3 = lst2 # ссылка

lst2[2] = "London"
print(lst2, lst3)

lst3 = lst2[:] # полное копирование  или lst3 = list(lst2)
lst2[2] = "Kiev"
print(lst2, lst3)
print(id(lst2), id(lst3), "Равны" if lst2 == lst3 else "Не равны")

marks = [1, 2, 3, 4, 5, 6, 7]
print(marks[2:-2])

# list(start:stop:step)
print(marks[1:5:2])
print(marks[::2])

# ------------------------------------ change list

marks[2:4] = ["3", "4"]
print(marks)

marks[:6:2] = [0, 0, 0]
print(marks)

marks[2:4] = 11, 22
print(marks)

# ----------------------------------------- > < != ==
print([1, 2, 3] > [1, 2, 3])
print([10, 2, 3] > [1, 2, 3])
print([1, 2, 3] >= [1, 2, 3])
print([1, 2, 3, 4] > [1, 2, 3])
# print([1, 2, 3] > [1, 2, "abc"]) error int > str

# --------- TASKS ______

m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[::-1][::2])

arr = ["a", "b", "c"]
arr.reverse()
print(arr)