print('......................................   abs() ')
a = -7
print(a)
print(abs(a))  # положительное число

print('......................................   min() ')
a = [1, 2, 3, 0, -5, 8, 10]
print('from array: ', a)
print('min is: ', min(a))

print('......................................   max() ')
print('from array: ', a)
print('max is: ', max(a))

print('......................................   pow() ')
a = 2 ** 3
print(a)

a = pow(2, 3)
print(a)

a = pow(27, 1 / 3)
print(a)

print('......................................   round() ')
a = 10.59488124
print(f'number {a} rounded..')
print(round(a))
print(round(a, 3))
print(round(a, 1))

print(round(a, -1))  # округление до десятков

a = 784.226649
print(f'number {a} rounded in -')
print(round(a, -1))
print(round(a, -2))

print('......................................   Вложенность ')

print("max(1, 2, abs(-3), -10) = ", max(1, 2, abs(-3), -10))
print("max(1, 2, abs(min(10, 5, -3)), 10) = ", max(1, 2, abs(min(10, 5, -3)), 10))

import math

print('......................................   math ')
print('......................................   ceil() ')

a = 10.2
print(math.ceil(a))
print(math.ceil(-a))

print('......................................   floor() ')
print(math.floor(a))
print(math.floor(-a))

print('......................................   factorial() ')
print(math.factorial(6))

print('......................................   trunc() ')
print(math.trunc(a))
print(int(a))

print('......................................   logarithm() ')
print(math.log(2.7185))
print(math.log2(4))
print(math.log10(1000))
print(math.ceil(math.log(1000, 10)))

print('......................................   Корень  sqrt')
print(math.sqrt(49))

print('......................................   sin cos ..... ')
print(math.sin(math.pi / 2), round(math.sin(3.14159265359 / 2)))

x = 20
print(math.floor(500 / (x - (x*0.1))))
