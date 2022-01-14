class Repo:
    def __init__(self, goldList, row: int, col :int) -> None:
        self.m_goldList = goldList
        self.m_row = row
        self.m_col = col
Repos = []
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    inputList = list(map(int, input().split()))
    goldList = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            goldList[i][j] = inputList[i*m + j]
    print(goldList)
    Repos.append(Repo(goldList, n, m))
    


class GoldMine:
    def __init__(self, goldList, row: int, col :int) -> None:
        self.m_goldList = goldList
        self.m_row = row
        self.m_col = col
        self.m_dy = [-1,0,1]
        self.m_d = [[-1]*col for _ in range(row)]

    def Solve(self) -> int:
        curMax = -1

        for j in range(self.m_col):
            for i in range(self.m_row):
                locMax = -1
                for z in self.m_dy:
                    curColIdx = j - 1
                    curRowIdx = i + z
                    if curColIdx < 0 or curRowIdx < 0 or curRowIdx + 1 > self.m_row:
                        continue
                    if self.m_d[curRowIdx][curColIdx] == -1:
                        continue
                    locMax = max(locMax, self.m_d[curRowIdx][curColIdx])
                if locMax == -1:
                    self.m_d[i][j] = self.m_goldList[i][j]
                else:
                    self.m_d[i][j] = locMax + self.m_goldList[i][j]

                curMax = max(curMax, self.m_d[i][j])
        print(self.m_d)
        return curMax


for aa in Repos:
    gm = GoldMine(aa.m_goldList, aa.m_row, aa.m_col)
    print(gm.Solve())


################
# 동빈나님 코드
################
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m) :
        for i in range(n) :
            # 왼쪽 위에서 오는 경우
            leftUp = 0
            if i == 0 :
                leftUp = 0
            else:
                leftUp = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            rightUp = 0
            if i == n - 1:
                rightUp = 0
            else :
                rightUp = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = max(leftUp, rightUp, left) + dp[i][j]

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
    