
n, m = map(int, input(">> ").split()); field = [list(input(">> ").strip()) for _ in range(n)]; print(sum(1 for i in range(n) for j in range(m) if field[i][j] == '.' and all(field[i+x][j+y] == '.' for x, y in [(0,1),(0,-1),(1,0),(-1,0)] if 0 <= i+x < n and 0 <= j+y < m)))
