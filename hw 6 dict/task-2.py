
n = int(input())

files = {}
for _ in range(n):
    line = input(">> ").split()
    name = line[0]
    rights = line[1:]
    files[name] = rights

n = int(input())

for _ in range(n):
    op, file = input(">> ").split()

    if op == "read":
        right = "R"
    elif op == "write":
        right = "W"
    elif op == "execute":
        right = "X"

    if right in files.get(file):
        print("-- OK")
    else:
        print("-- Access denied")