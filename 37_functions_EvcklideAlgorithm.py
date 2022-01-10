import time

a = 18
b = 24


def get_nod(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД(a, b)
    """
    # while b != 0:
    #     a, b = b, a % b
    # return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_nod_fast(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b по алгоритму Евклида
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД(a, b)
    """
    while b != 0:
        a, b = b, a % b
    return a


def test_nod(func):
    # --- тест №1 ---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('Test #1 OK')
    else:
        print('Test #1 FAILED')

    # --- тест №2 ---
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('Test #2 OK')
    else:
        print('Test #2 FAILED')


    # --- тест №3 ---
    a = 2
    b = 10000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('Test #3 OK', dt)
    else:
        print('Test #3 FAILED', "{:.20f}".format(dt))

res = get_nod(18, 24)
print(res)
help(get_nod)


test_nod(get_nod)
test_nod(get_nod_fast)