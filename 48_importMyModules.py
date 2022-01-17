import ex_48_module
# a = my.floor(3.7)
# print(a)

#from ex_48_module import floor
import pprint


#a = floor(3.7)
from folder import ex1

pprint.pprint(dir(ex_48_module))

print(ex_48_module.time.time()) # time импортированна из модуля ex_48_module

import sys
pprint.pprint(sys.path)

ex1.main()

# Повторно импортировать модуль
import importlib
importlib.reload(ex_48_module)


