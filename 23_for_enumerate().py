n = int(input("Enter a number: "))
if n < 1 or n > 100:
    print("Invalid number")
else:
    p = 1
    for i in range(1, n + 1):
        p *= i
    print("The factorial of", n, "is", p)

# ёлка
for i in range(1, 7):
    print("*" * i)

#

words = ["привет", "пока", "как дела", "пока"]
s = ""
for w in words:
    s += w + " "
print(s)

digits = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digits)):
    if 10 <= abs(digits[i]) <= 99:
        digits[i] = 0
print(digits)

print('................................................................ enumerate ()')
digits = [4, 3, 100, -53, -30, 1, 34, -8]

for i, d in enumerate(digits):
    if 10 <= abs(d) <= 99:
        digits[i] = 0
print(digits)

print('................................................................ Преобразование кириллицы в латиницу')
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i','y',  'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch',
     'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = "Программирование на Python - от первого к последнему символу"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index ]
    elif s == "ё":
        slug += "yo"
    elif s in " !?.,;:":
        slug += '-'
    else:
        slug += s

if "--" in slug:
    slug = slug.replace("---", "-")
print(slug)
