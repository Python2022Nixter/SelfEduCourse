# (<формирование значения> for <переменная> in <итеррируемый обьект>)

gen = (x ** 2 for x in range(10))
for i in gen:
    print(i)

for i in gen:
    print(i)  # второй раз нельзя вызвать генератор

a = (x ** 2 for x in range(6))
print("sum: ",sum(a))
a = (x ** 2 for x in range(6))
print("max: ",max(a))
a = (x ** 2 for x in range(6))
print("min: ",min(a))
a = (x ** 2 for x in range(6))
b = list(a)
print(b)

lst = (x for x in range(10000))
for i in lst:
    if i % 1000 == 0:
        print(i)

