
num = int(input(">> "))
lst = [(str(i) + " ") * i for i in range(1, num)]
print("".join(lst)[:num*2])
