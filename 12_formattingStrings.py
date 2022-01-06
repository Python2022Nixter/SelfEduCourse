
# ------------------------------------------  String.format(*ags)

age = 44
name = "Nikolay"

print("My name is {0}, age is {1}, i love Beer".format(name, age))
print("My name is {fio}, age is {old}, i love Beer".format(fio=name, old=age))
print(f"My name is {name.upper()}, age is {int(age // 3)}, i love Beer")    #  PEP 498 -- Literal String Interpolation


# ----
a, b = float(input()), int(input())

print(f"Вы можете получить {int(b // a)}$ за {b} рублей по курсу {a}")
