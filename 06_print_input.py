print("....................................   print()")

print(".....................   Разделители")

# set= разделитель ( поумолчанию = "" )
# end= окончание строки ( поумолчанию = "\n" )

a = 6.81
b = 2
c = 25.25

print(a, b, c, sep=" | ")
print(a, b, c, sep="; ")
print(a, b, c, sep=" ___ ")

print("Hello", end=" ")
print("Nikolay")

print(".....................   Formatting")

x = 5.76
y = -8

print("координаты точки: x = ", x, "; y = ", y, sep="")
print(f"координаты точки: x = {x}; y = {y}")

print(".......................................   input()")

a = input()
print(a, type(a))

b = float(input('enter number ONLY'))
# b = int(b)
b = abs(b)
print(b)


a = float(input('num a  '))
b = float(input('num b  '))
print("Периметр: ", 2 * (a + b))

a, b = map(float, input(" enter number  ").split())
print("Периметр: ", 2 * (a + b))

a, b, c = map(int, input("triangle: ").split())
print("периметр: ", a+b+c)