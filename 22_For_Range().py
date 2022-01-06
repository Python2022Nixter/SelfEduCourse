print("....................................................... for")

d = [1, 2, 3, 4, 5]
for x in d:
    print(x)

for x in "python":
    print(x)

for i in d:
    if i == 3:
        d[i-1] = True
    print(x)
print(d)

print("................................................ range()")
a = list(range(5))
b = list(range(2, 7))
c = list(range(10, 70, 10))
print(a, b, c)
a = list(range(-10, -20, -2))
print("reverse:" , a)

# from 5 to 0
a = list(range(5, -1, -1))
print(a)


for i in range(5):
    d[i] = 0
print(d)

# primer
s = 0.0
n = 1000

for i in range(2, n + 1):
    s += 1 / i
print(s)