import sys
from sys import getsizeof

#
res = sys.maxsize
print(type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))

res = res * res
print( type(res), res)
print('size: ', getsizeof(res))
#

print('......................................................... операторы')

d =   8 / 2
print(d)

d2  = 3/ 6
print(d2)

d3 = 7 // 2 # целочисленное деление
print(d3)

d3 = -7 // 2
print(d3) # округляется вверх у целочисленному значению


# ........................................ остаток от деления
d4 = 10 % 3 # [3.. , 3.. , 3.. ,1]
print(d4)

d5 = 9 % 5
print(d5) # 4

d5 = -9 % 5
print(d5) # 1

d5 = -9 % -5
print(d5) # -4

d5 = 9 % -5
print(d5) # -1


# ................................................. возведение в степень
print('********************************************')

d6  = 2 ** 3
print(d6)

d6 = 36 ** 0.5
print( '√36: ', d6) # квадратный корень √36

d6  = 2 ** 3 ** 2
#     ︎⬅   ︎⬅   ︎⬅   ︎⬅
print(d6)
