# N x M 크기의 직사각형 형태의 미로에 갖혔다. 미로에는 여러마리의 괴물이 있어 이를 피해 탈출해야 한다.
# 현재 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 괴물이 있는 부분은 0으로 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출가능한 형태로 제시 된다.
# 이때 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오. 시작칸과 마지막 칸을 모두 포함하여 계산한다.

from typing import List
from collections import deque

class MazeEscape:
    def __init__(self, graph : List[List[int]]) -> None:
        self.m_graph = graph
        self.m_col = len(self.m_graph[0])
        self.m_row = len(graph)

    def Solve(self) -> int:
        self.BFS()
        return self.m_graph[self.m_row -1][self.m_col-1]

    def BFS(self) -> None:
        queue = deque()
        queue.append((0,0))
        while queue:
            row, col = queue.popleft()
            
            if row == self.m_row - 1 and col == self.m_col - 1:
                return

            tt = [-1, 0, 1]
            for tr in tt:
                for tc in tt:
                    if abs(tr) == 1 and abs(tc) == 1:
                        continue
                    if tr == 0 and tc == 0 :
                        continue
                    tRow = row + tr
                    tCol = col + tc
                    if self.CheckValidate(tRow, tCol):
                        queue.append((tRow, tCol))
                        self.m_graph[tRow][tCol] = self.m_graph[row][col] + 1

    def CheckValidate(self, row : int, col : int) -> bool:
        if row < 0 or row > self.m_row - 1 or col < 0 or col > self.m_col - 1:
            return False
        if self.m_graph[row][col] == 0:
            return False

        return True

        
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

me = MazeEscape(graph)
print(me.Solve())


# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 벗어난 경우 무시 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드 처음 방문하는 경우만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# 가장 오른쪽 아래까지의 최단 거리 반환
print(graph[N-1][M-1])
