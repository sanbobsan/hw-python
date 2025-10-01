
lst = list()

while True:
    i = int(input(">> "))
    lst += [i]
    if not sum(lst):
        break

print(sum([i**2 for i in lst]))
