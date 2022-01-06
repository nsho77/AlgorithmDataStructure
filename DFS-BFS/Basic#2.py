# DFS 기초
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 1번 노드부터 있다고 가정
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]    
]

# 각 노드가 방문한 정보를 표현 (1차원 리스트)
visited = [False] * 9


def DFS(graph, v, visited) -> None:
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드 재귀방문
    for vv in graph[v]:
        if visited[vv] == False:
             DFS(graph, vv, visited)

DFS(graph, 1, visited)
print()

# BFS 기초
from collections import deque

visited = [False] * 9

def BFS(graph, v, visited) -> None:
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        nv = queue.popleft()
        print(nv, end=' ')
        for vv in graph[nv]:
            if not visited[vv]:
                visited[vv] = True
                queue.append(vv)

BFS(graph, 1, visited)