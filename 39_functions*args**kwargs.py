def text_args(*args, sep="\\", **kwargs): # оператор упаковки параметров
    print(type(args))
    print(kwargs)
    if 'trim' in kwargs and kwargs['trim']:
        args = [arg.strip() for arg in args]
    str = sep.join(args)
    print(str)

text_args("Prevet \\ Nikolay, ", "Ivanov  ", "   Petrov", " Sidorov    ", sep=" /\\ ", trim=True)