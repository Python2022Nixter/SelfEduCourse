x = int(input())

if x % 2 == 0:
    if 0 <= x <= 9:
        print("цифра")
    else:
        print("число")
else:
    print("х - нечётное")


print("============  max ")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b:
    if a > c:
        print("a -> max")
    else:
        print("c -> max")
else:
    if b > c:
        print(("b -> max"))
    else:
        print("c -> max")

print("============  courses")

item = int(input("item: "))
if item == 1:
    print("Python")
elif item == 2:
    print("C++")
elif item == 3:
    print("Java")
else:
    print("JavaScript")

print("============ finish")

number = int(input())
if number < 0:
    print("Число должно быть положительным")
elif 0 <= number <= 9:
    print("цифра")
elif 10 <= number <= 99:
    print("число")
elif number in range(100, 999):
    print("трехзначное число")
