import heapq

g_N, g_M, g_C = map(int,input().split())
g_graph = [[] for _ in range(g_N + 1)]
for _ in range(g_M):
    x, y, z = map(int, input().split())
    g_graph[x].append((y, z))

class MessageSend:
    def __init__(self, _graph, _N, _M, _C) -> None:
        self.m_graph = _graph
        self.m_N = _N
        self.m_M = _M
        self.m_C = _C
        self.INF = int(1e9)
        self.m_time = [self.INF] * (self.m_N + 1)

    def Solve(self) -> None:
        priorityQ = []
        self.m_time[self.m_C] = 0
        heapq.heappush(priorityQ, (0, self.m_C))

        while priorityQ:
            time, city = heapq.heappop(priorityQ)
            if self.m_time[city] < time:
                continue

            for ii in self.m_graph[city]:
                icity, itime = ii
                if self.m_time[icity] > self.m_time[city] + itime:
                    self.m_time[icity] = self.m_time[city] + itime
                    heapq.heappush(priorityQ, (self.m_time[icity], icity))

        totalConnectedCity = 0
        totalTime = 0
        for i in range(1, self.m_N + 1):
            if self.m_time[i] != self.INF and i != self.m_C:
                totalConnectedCity += 1
                totalTime = max(totalTime, self.m_time[i])
        print("{0} {1}".format(totalConnectedCity, totalTime))

ms = MessageSend(g_graph, g_N, g_M, g_C)
ms.Solve()

##############
# 동빈나님 코드
##############
INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n + 1)

def dijkstraPriorityQueue(_start : int) -> None:
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 다익스트라 알고리즘 수행
dijkstraPriorityQueue(start)

# 도달할 수 이 있는 노드 수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드 제외해야 하므로 count - 1 출력
print(count -1, max_distance)