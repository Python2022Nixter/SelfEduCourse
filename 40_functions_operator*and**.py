x, y,  = (1, 2)
print(x, y)

print("................................................................распаковка кортежей")
x, *y = (1, 2, 3, 4, 5)
print(x, y)

a = [1, 2, 3, 4, 5]
print(a)
print(*a)


d = -5, 5
res = list(range(*d))
print(res)
r = range(2,8)
r2 = list(r)
print(r)
print(*r)
print("range(): {0}, *range(): {1}".format(r, *r))  # так и не понял почему не работает

print("................................................................распаковка словарей")
d = {1:'Kiev', 2:'Odessa', 3:'Lviv'}
print(d)
print(*d)
print(*d.values())
print(*d.keys())
print(*d.items())

print("................................................................слединение словарей")
d = {1:'Kiev', 2:'Odessa', 3:'Lviv'}
с = {4:'Kharkiv', 5:'Dnipro'}
{**d, **с}
print(d)