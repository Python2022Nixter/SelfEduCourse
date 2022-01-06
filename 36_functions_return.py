def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res, x


print(get_sqrt(49))


def get_max(a, b):
    return a if a > b else b


a, b = get_sqrt(49)
print(get_max(a, b))

print("................................................................ get_max3")


def get_max3(a, b, c):
    return get_max(a, get_max(b, c))


x, y, z = 5, 7, 10
print(get_max3(x, y, z))


print("................................................................ периметр или площадь")

PERIMETR = False
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b


print("True", get_rect(1.5, 3.8))
