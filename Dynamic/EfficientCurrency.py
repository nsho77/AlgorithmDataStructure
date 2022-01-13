from typing import List

N,M = map(int, input().split())
l = [0] * N
for i in range(N):
    l[i] = int(input())

class EffCurrency:
    def __init__(self, ll : List[int], t : int) -> None:
        self.m_cl = ll
        self.m_target = t
        self.m_d = [10001] * (t + 1)

    def Solve(self) -> int:
        for i in range(1, self.m_target+1):
            locMin = 10001
            for currency in self.m_cl:
                curCurrency = i - currency
                if curCurrency < 0 :
                    continue
                if curCurrency == 0:
                    locMin = 1
                    break
                locMin  = min(locMin, self.m_d[i - currency] + 1)
            self.m_d[i] = locMin
        if self.m_d[self.m_target] == 10001:
            return -1
        else:
            return self.m_d[self.m_target]

ec = EffCurrency(l, M)
print(ec.Solve())


###############
# 동빈나님 코드
###############
array = []
for i in range(N):
    array.append(int(input()))
d = [10001] * (M + 1)
d[0] = 0

for i in range(N):
    for j in range(array[i], M+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])

     
    