from tokenize import String

s1 = "Panda"
s2 = 'Panda'

text = '''Я Python выучил бы только за то,
что есть популярные курсы.
Много хороших курсов'''

print(s1, s2 , '\n',  text)

a = ""
a = " "
s1 = "Я люблю"
s2 = "язык SwiftUI & Python"
print( s1 + " " + s2) # конкатенация = соединение строк
print( s1 + " " + s2 + " " + str(3))

print("................................................................ Дублирование, длина, содержит ли?")
a = "ha "
print(a * 5) # int number ONLY

print("length: ", len(a))
print("length: ", len(a * 5))

a = "Nikolay"
b = "kola"

print(b in a)

print(".................................................................. Сравнение")

print( a == b)
a = 'Nikolay'
b = 'nikolay'
print(a == b.capitalize())

a = "kot"
b = "kit"

print(a > b)
a = "Kit"
b = "kit"

print(a > b)

# Узнать код символа ASCII ..... ord()

print("K", ord('K'))
print("k", ord('k'))
# 75 > 107 = False

