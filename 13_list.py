print("________________________________________________________________ list")

marks = ["Tel Aviv", "New York", "Tokio"]
print(marks)
print(marks[0])

ball = [2, 4, 5, 3, 4, 3, 5]
print(ball[0])
print(ball[-1])

#+  0  1  2  3  4  5  6
#  [2, 4, 5, 3, 4, 3, 5]
#- -7 -6 -5 -4 -3 -2 -1

res = (sum(ball) / len(ball))
print(res)

ball[0] = 5
res = (sum(ball) / len(ball))
print(res)
lst = ["wer", 45, 2.2, True]
lst2 = [12, 22, lst, ball]
print(lst2)

a = list([True, False])
print(a)
b = list("python")  # итеррированный
print(b) # итеррированный


print("________________________________________________________________ functionality")

t = [15.6, 21.0, 14.22, 12.0, 16.4, 17.0]
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t) / len(t))
t_sorted = sorted(t, reverse=True)
print(t_sorted)

p = list("python")
print(sorted(p))
print(max(p))
print(min(p))
print("________________________________________________________________ Operators")

a = [1, 2, 3] + [4, 5]  # list + list        : [1, 2, 3] + [4]   !!!!!!
b = ["I", "Love", "Beer"] * 3
print(a, b)
c = ["I"] + ["Love"] * 3 + ["Wine"]
print(c)

print( 2 in a)
print( "Love" in c)

# ________________________________________________________________

# a = list(map(str, input().split()))
# print(a)

# a = list(map(int, input().split()))
# print(*sorted(a, reverse=True))

# a = list(map(str, input().split()))
# cities = ["Москва", "Тверь", "Вологда"]
# lst = cities + a
# print(*lst)
