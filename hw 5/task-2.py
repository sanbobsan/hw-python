s = input(">> ").strip()
LENGHT = len(s)

previous, current = "", ""
total_index = 0
n = 1
while True:
    str_n = str(n)
    current = previous + str_n
    total_index += len(str_n)
    if s in current:
        id = current.find(s)
        print(total_index + id - len(current) + 1)
        break
    previous = current[-LENGHT:]
    n += 1
