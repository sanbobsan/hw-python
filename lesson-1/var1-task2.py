
a, b, c, d, e = map(int, input(">> ").split())
res = 0

for x in range(1001):
    if (a*x**3 + b*x**2 + c*x + d) == 0:
        res += 1

print(res)
