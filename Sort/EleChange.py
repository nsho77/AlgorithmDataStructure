# 두 배열의 원소 교체

N, K = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

class EleChange:
    def __init__(self, arrA, arrB, _K) -> None:
        self.m_arrA = arrA
        self.m_arrB = arrB
        self.m_k = _K

    def Solve(self) -> int:
        self.m_arrA.sort()
        self.m_arrB.sort(reverse = True)

        for i in range(self.m_k):
            if self.m_arrA[i] < self.m_arrB[i]:
                self.m_arrA[i], self.m_arrB[i] = self.m_arrB[i], self.m_arrA[i]
            else:
                break
        
        return sum(self.m_arrA)

ec = EleChange(arrA, arrB, K)
print(ec.Solve())
