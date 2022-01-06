print(".........................................   Boolean")

a, b = map(int, input().split())

print(a % b == 0)

y = 1.85
print(y >= -2 and y <= 5)  # &&
print(y < -2 or y > 5)
# ==
print(-2 <= y <= 5)


#              Priority:
#    or  1
#    and 2
#    not 3

x = 7
print("x...", not (x % 2 == 0 or x % 3 == 0))

print("................................  Boolean with String")

a = bool("")
print("clean a: ", a)
a = bool("test")
print("test a: ", a)

