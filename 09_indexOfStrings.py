s = 'hello python'

print(s[0])

index = len(s) - 1

print(s[index])
# ==
print('s[-1]  ',s[-1])

print("................................................................ срезы")

print(s[3:6])
print(s[7:10])
print(s[-4:-1])

a = s[:]

print(id(s), id(a))

print("................................................................ steps")
# string[start:stop:step]
alph = "abcdefghijklmnopqrstuvwxyz"
print(alph[0:20:2])
print(alph[::-1])

s2 = "H" + s[1:]
print(s2)

# -------------- testing
a = "Hello"
b = "Hell"
a = a[:len(b)][::2]
b = b[::2]
print("_",a[:len(b)][::2] == b[::2])