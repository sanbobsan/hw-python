
count = int(input(">> "))
cells = {tuple(map(int, input(">> ").split())) for _ in range(count)}

count = 0
for row, col in cells:
    for d_row, d_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (row + d_row, col + d_col) not in cells:
            count += 1

print(count)