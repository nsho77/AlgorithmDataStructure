N,M = map(int, input().split())
cakeArray = list(map(int, input().split()))

class RiceCakeMaking:
    def __init__(self, array, arrayLen:int, reqLength:int ) -> None:
        self.m_arr = array
        self.m_arrLen = arrayLen
        self.m_reqLen = reqLength

    def Solve(self) -> int:
        maxHeight = 2000000000
        left = 0
        right = maxHeight
        while left < right:
            mid = (left + right) // 2
            spareLength = 0
            # Get 자른 길이 합
            for i in self.m_arr:
                if mid < i :
                    spareLength += i - mid
            if self.m_reqLen == spareLength:
                return mid
            elif self.m_reqLen > spareLength:
                right = mid - 1
            else :
                left = mid + 1
        
        return left

rcm = RiceCakeMaking(cakeArray, N, M)
print(rcm.Solve())


###############
# 동빈나님 코드
###############
N,M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < M:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else :
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result에 기록
        start = mid + 1

print(result)

