N = int(input())
foodList = list(map(int, input().split()))

class AntWarrior:
    def __init__(self, foodList) -> None:
        self.m_foodList = foodList
        self.m_dp = [0] * 2

    def Solve(self) -> int:
        self.m_dp[1-1] = self.m_foodList[0]
        self.m_dp[2-1] = max(self.m_foodList[0], self.m_foodList[1])
        nowLen = 3
        for i in range(nowLen, len(self.m_foodList) + 1):
            temp = self.m_dp[1]
            self.m_dp[1] = max(self.m_dp[0] + self.m_foodList[i - 1], self.m_dp[1])
            self.m_dp[0] = temp
        
        return self.m_dp[1]


aw = AntWarrior(foodList)
print(aw.Solve())


# /*동빈나님의 코드*/
n = int(input())
array = list(map(int, input().split()))

# dp table
d = [0] * 100

# 바텀업 방식
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])