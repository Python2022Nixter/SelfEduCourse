# import math as mt  # Теперь можно использовать имя пакета в качестве префикса
# from math import pi, ceil
from  math import *  # Импортирует все имена из пакета math
import pprint


# print(locals())
pprint.pprint(locals())
# a = mt.ceil(1.8)
# print(a)
#
# print(mt.pi)

print(pi)
print(ceil(1.8))

import datetime

a = datetime.datetime.now()
print(a, type(a), datetime.datetime.astimezone(a))

######################
# Задачи
######################

# Задача-1:
import math
a = float(input())
print(math.ceil(a))
