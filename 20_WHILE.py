
N = 1_000
s = 0
i = 1

while i <= N and i <= 50:
    s += i
    i += 2
print(s)

i = 1
while i < 10:
    print(i)
    i += 1

N = -10
i = -1
while i >= N:
    print(i)
    i -= 1

print("................................................................ pass")
pass_true = "password"
ps = ""

while ps != pass_true:
    ps = input(" enter password: ")
print("entry successful")

print("................................................................ % 3")
N = 100
i = 1
while i <= N:
    if i % 3 == 0:
        print(i)
    i += 1