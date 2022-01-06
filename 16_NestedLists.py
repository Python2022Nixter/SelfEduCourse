
line = [1, 2, 3, 4, 5]

img = [[1, 2, 3], [1, 2, 3], line[:]]
print(img)
print(img[0])
print(img[0][1])

img[1] = [0] * 5
print(img)

img[1][:] = [1] * 5
print(img)

del img[1]
print(img)
# --------------------------

A = [[[True, False], [1, 2, 3]], ["matrix", "vector"]]
print(A[0])
print(A[0][1][0])
print(A[1])


#--------
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

a = input() # дядя
print(a in t[0] or a in t[1] or a in t[2])




