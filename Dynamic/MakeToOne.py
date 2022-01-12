X = int(input())

class MakeToOne:

    def __init__(self) -> None:
        self.m_dp = [0] * 30001
        
    def Solve(self, a : int) -> int:
        if a == 1 : return 0

        if self.m_dp[a] != 0:
            return self.m_dp[a]
        
        l = []
        if a % 5 == 0:
            l.append(a//5)
        if a % 3 == 0:
            l.append(a//3)
        if a % 2 == 0:
            l.append(a//2)
        l.append(a-1)

        ll = []
        for i in l:
            ll.append(self.Solve(i))

        self.m_dp[a] = min(ll) + 1
        return self.m_dp[a]
        
mo = MakeToOne()
print(mo.Solve(X))

################
# 동빈나님 코드 #
################

d = [0] * 30001

for i in range(2, X+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5] + 1)

print(d[X])