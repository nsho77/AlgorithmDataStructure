# NxM 크기의 얼음 틀이 있따. 구멍이 뚫려 있는 부분은 0, 칸막이 있는 부분은 1이다.
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결된 것으로 간주
# 얼음 틀 모양이 주어질 때 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성하라.

from collections import deque
from typing import List

class IceBeverage:
    def __init__(self, graph : List[List[int]]) -> None:
        self.m_graph = graph
        self.m_col = len(graph[0])
        self.m_row = len(graph)
        self.m_res = 0 # 얼음 틀 개수

    def Solve(self) -> int:
        for i in range(self.m_row):
            for j in range(self.m_col):
                if self.m_graph[i][j] == 1:
                    continue
                elif self.m_graph[i][j] == 2:
                    continue
                else:
                    self.BFS(i, j)
                    self.m_res += 1
        return self.m_res

    def BFS(self, row : int, col : int) -> None:
        queue = deque()
        queue.append((row, col))
        while queue:
            lRow, lCol = queue.popleft()
            self.m_graph[lRow][lCol] = 2
            rr = [-1, 0, 1]
            for ri in rr:
                for ci in rr:
                    if ri == ci : continue
                    llRow = lRow + ri
                    llCol = lCol + ci
                    if self.CheckBound(llRow, llCol) :
                        if self.m_graph[llRow][llCol] != 2:
                            queue.append((llRow, llCol))

    def CheckBound(self, row : int, col : int) -> bool:
        if self.m_row < row + 1 or self.m_col < col + 1 :
            return False
        elif row < 0 or col < 0:
            return False
        
        if self.m_graph[row][col] == 1:
            return False

        return True


graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0],
]
ic = IceBeverage(graph)
print(ic.Solve())

#/*
# 다른 풀이
#*/
# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS 로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y)-> bool:
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:    
        # 해당 노드 방문 처리
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    else:
        return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS수행
        if dfs(i, j) == True:
            result += 1

print(result)