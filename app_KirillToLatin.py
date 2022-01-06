import sys

print(sys.version)

# a, b = map(int, input().split())
#

print('................................................................ Преобразование кириллицы в латиницу')
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
     'z', 'i','y',  'k', 'l', 'm', 'n', 'o', 'p',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch',
     'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = "Программирование на Python - от начала до конца"
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