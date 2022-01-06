# remove(), pop(), clear(), copy(), count(), index(), reverse(), sort()

a: list[int] = [1, -54, 3, 23, 43, -45, 0]
print("................................................................ append() ")
a.append(100)
print(a)

# not this !!!!!!!!!!!!!!!!!!!!
a = a.append(40)
print(a)  # = None

a = [1, -54, 3, 23, 43, -45, 0]
a.append(True)
print(a)

print("................................................................ insert()")
a.insert(3, -1000)
print(a)
print("................................................................ remove()")

a.remove(True) # deleting 1 !!!!         True = 1, False = 0
print(a)

a.remove(True) # deleting True !!!!!!!
print(a)

# a.remove(1000000) # ERRROR!!

print("................................................................ pop()")
end = a.pop()
print(a, end)

a.pop(3)
print(a)

a.clear()
print(a)

print("................................................................. copy() ")
a = [1, -54, 3, 23, 43, -45, 0]
c = a.copy()
print(a, c, id(a), id(c), "True" if id(a) == id(c) else "False")

print("................................................................ count()")
print(a.count(23))
a.append(1)
print(a.count(1))

print("................................................................  index()")
print(a.index(1))
print(a. index(1, 2))

# print(a.index("ff"))  # ERROR
if "ff" in a:
    print(a.index("ff"))
else:
    print("NotImplemented")

print("............................................................... sort()")

a.sort()
print(a)

a.sort(reverse=True)
print(a)

# ---------- TASKS



