
n = int(input(">> "))
passengers = [tuple(map(int, input(">> ").split())) for _ in range(n)]
t = int(input(">> ")); res = 0

for a, b in passengers:
    if a <= t <= b: res += 1
print(res)
