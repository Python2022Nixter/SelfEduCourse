def get_V(a, b, c, verbose=True):
    '''
    Calculate the volume of a right-angled triangle
    :param a: natural number
    :param b: natural number
    :param c: natural number
    :return: a * b * c
    '''
    if verbose:
        print(f"a = {a}, b = {b}, c = {c}")
    return a * b * c


v = get_V(2, 3, 4)
print(f"v = {v}")

v = get_V(c=2, b=3, a=4)  # можно присваивать по имени аргумента
print(f"v = {v}")
# help(get_V)

v = get_V(2, 3, 4, verbose=False)
print(f"v = {v}, verbose = False")

print("..................................................... сравнение строк  + параметры по умолчанию")


def cmp_str(s1, s2, reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    return s1 == s2


print(cmp_str("Python ", " Python"))
print(cmp_str("Python ", " Python", trim=False))
print(cmp_str("Python ", " PYTHON", reg=False, trim=False))

print("..................................................... add values")


def add_value(value, lst=[]):
    lst.append(value)
    return lst

l = add_value(1)
l = add_value(2)
print(l)

def add_value2(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

l = add_value2(1)
l = add_value2(2)
print(l)

print(add_value2(3, l))
