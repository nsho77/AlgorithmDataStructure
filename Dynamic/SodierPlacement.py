N = int(input())
sol = list(map(int, input().split()))

class SoldierPlacement:
    def __init__(self, soldierList, n : int) -> None:
        self.m_soldierList = soldierList
        self.m_n = n
        self.m_d = [1] * n

    def Solve(self) -> int:
        for i in range(1, self.m_n):
            for j in range(0, i + 1):
                if self.m_soldierList[j] > self.m_soldierList[i]:
                    self.m_d[i] = max(self.m_d[i], self.m_d[j] + 1)

        return self.m_n - max(self.m_d)



sp = SoldierPlacement(sol, N)
print(sp.Solve())

##################
# 동빈나님 코드
##################

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
dp = [1]* n
# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i+1):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외하는 병사 최소 수 출력
print(n - max(dp))