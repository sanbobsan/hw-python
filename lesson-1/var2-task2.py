
a, b, c, d = map(int, input(">> ").split())

lst = []
for x in range(1001):
    if (a*x**3 + b*x**2 + c*x + d) == 0:
        lst.append(x)

try:
    lst[0]
    print(*lst[::-1])
except IndexError:
    pass
