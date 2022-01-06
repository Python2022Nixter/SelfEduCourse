s = 'python'
print(type(s))

print('upper',s.upper())
res = s.upper()
print('res', res)
print('lower of res', res.lower())

print('................................ count')
#String.count(sub[, start[, end]])

msg = 'abrakatabra'
print(msg.count("ra")) # 2
print(msg.count("ra", 4)) # 1, search from index 4
print(msg.count("ra", 4, 10)) # last index not included!!!!

print('................................................find')
#String.find(sub[, start[, end]])

print(msg.find("br"))
print(msg.find("br", 5))
print(msg.find("brr"))

print('................................................ rfind')
#String.rfind(sub[, start[, end]])

print(msg.rfind('br'))

print('.............................................. index')
#String.index(sub[, start[, end]])

print(msg.index('br', 5))

print('.................................................. replace')
#String.replace(old, new, count=-1)

print(msg.replace('a', 'o'))
print(msg.replace('ab', 'AB'))

print('............................................ isalpha')
print(msg.isalpha())
s = "hello www"
print('s isalptha ', s.isalpha())

print('............................................ isdigit')
print(msg.isdigit())
s = "1522"
print('s is digit ', s.isdigit())

print('............................................ rjust')
#String.rjust(width[, fillchar=''])
s = "abc"
print(s.rjust(5))
d = '12'
print(d.rjust(12, '0'))

print('............................................ ljust')
#String.rjust(width[, fillchar=''])
s = "abc"
print(s.ljust(5))
d = '12'
print(d.ljust(12, '*'))

print('.......................................................... split')
# String.split(sep=None, maxsplit=-1)
# sep - разбитиие строки

print("Nikolaenko Nikolay Nikolaevich".split(' '))

digs = "1, 2,3,  4,5, 6"
print(digs.replace(" ", "").split(","))

print('................................................................... join')
# String.join(list)
d = digs.replace(" ", "").split(",")
print(" | ".join(d))

print("....................................................... strip")
s = '      hello word   \n'
print(s)
print(s.strip())
print(s.rstrip())
print(s.lstrip())

#----------
s = 'Москва Тверь Казань'
print(";".join(s.split(" ")))