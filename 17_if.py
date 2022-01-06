x = -4
if x < 0:
    x = -x
print(x)

a = float(input("a: "))
b = float(input("b: "))

if a < b:
    a, b = b, a
print(a, b)

x = int(input("x in range: "))
if x >= -4 and x <= 10:
    print("x in range [-4:10]")


x = (input(" true false"))
if x:
    print("x True")


marks = [3, 3, 2, 4, 5]

if 2 in marks:
    print("nahuy")
else:
    print("good man")