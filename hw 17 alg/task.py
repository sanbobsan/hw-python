from heapq import heappush, heappop


def read_input():
    n, m = map(int, input().split())

    heights = []
    for _ in range(n):
        row = list(map(int, input().split()))
        heights.append(row)

    start_r, start_c = map(int, input().split())
    cargo_r, cargo_c = map(int, input().split())
    finish_r, finish_c = map(int, input().split())

    return n, m, heights, start_r, start_c, cargo_r, cargo_c, finish_r, finish_c


def build_graph(n, m, heights):
    graph = [[] for _ in range(n * m)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            current = i * m + j

            for dx, dy in moves:
                ni, nj = i + dx, j + dy

                if 0 <= ni < n and 0 <= nj < m:
                    if abs(heights[i][j] - heights[ni][nj]) <= 100:
                        neighbor = ni * m + nj
                        graph[current].append(neighbor)

    return graph


def dijkstra(start, target, graph, total_nodes):
    distances = [float("inf")] * total_nodes
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        dist, node = heappop(queue)

        if node == target:
            return dist

        if dist > distances[node]:
            continue

        for neighbor in graph[node]:
            new_dist = dist + 1

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heappush(queue, (new_dist, neighbor))

    return float("inf")


def manhattan(idx1, idx2, m):
    x1, y1 = divmod(idx1, m)
    x2, y2 = divmod(idx2, m)
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(start, target, graph, n, m):
    g_score = [float("inf")] * (n * m)
    g_score[start] = 0
    f_score = [float("inf")] * (n * m)
    f_score[start] = manhattan(start, target, m)

    queue = [(f_score[start], start)]

    while queue:
        current_f, current = heappop(queue)

        if current == target:
            return g_score[current]

        if current_f > f_score[current]:
            continue

        for neighbor in graph[current]:
            tentative_g = g_score[current] + 1

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + manhattan(neighbor, target, m)
                heappush(queue, (f_score[neighbor], neighbor))

    return float("inf")


def main() -> None:
    n, m, heights, sr, sc, cr, cc, fr, fc = read_input()

    start = sr * m + sc
    cargo = cr * m + cc
    finish = fr * m + fc
    graph = build_graph(n, m, heights)

    dist1 = dijkstra(start, cargo, graph, n * m)
    dist2 = dijkstra(cargo, finish, graph, n * m)

    result = dist1 + dist2
    print("Dijkstra: ", result)

    dist1 = a_star(start, cargo, graph, n, m)
    dist2 = a_star(cargo, finish, graph, n, m)

    result = dist1 + dist2
    print("A*: ", result)


if __name__ == "__main__":
    main()
