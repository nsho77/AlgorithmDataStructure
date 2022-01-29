INF = int(1e9)
g_N, g_M = map(int, input().split())
g_graph = [[INF] * (g_N + 1) for _ in range(g_N + 1)]
for _ in range(g_M):
    a, b = map(int, input().split())
    g_graph[a][b] = 1
    g_graph[b][a] = 1

g_X, g_K = map(int, input().split())

for a in range(1, g_N + 1):
    for b in range(1, g_N + 1):
        if a == b:
            g_graph[a][b] = 0

for k in range(1, g_N + 1):
    for a in range(1, g_N + 1):
        for b in range(1, g_N + 1):
            g_graph[a][b] = min(g_graph[a][b], g_graph[a][k] + g_graph[k][b])

distance = g_graph[1][g_K] + g_graph[g_K][g_X]

if distance >= INF:
    print(-1)
else:
    print(distance)
