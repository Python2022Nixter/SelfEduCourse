# break - досрочное завершение оперпции
# continue - пропуск лдной итерации

print("Start Loop...")
i = 0
while True:
    i += 1
    break
print("End Loop...")

#----------------------------------------------

d = [1, 5, 3, 6, 0, -4]
flFind = False
i = 0
while i < len(d):
    flFind = d[i] % 2 == 0
    if flFind:
        break

    i += 1
print(flFind)

# ---------------------------------------------
s = 0
d = 1

while d != 0:
    d = int(input("Ebter int number: "))
    if d % 2 == 0:
        continue # пропускает всё что написанно ниже

    s += d
    print("s = " + str(s))

print(".......................................... else")
# s = 1/2 + 1/3 + 1/4 + ... 1/0

s = 0
i = -10

while i < 0: # i < 100
    if i ==0:
        break
    s += 1/i
    i += 1
else:
    print("correct sum")
print(s)

