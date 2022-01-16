from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

class CountOfNum:
    def __init__(self, _N: int, _array, _x:int) -> None:
        self.m_arrayLen = _N
        self.m_array = _array
        self.m_target = _x

    def UseBisect(self) -> int:
        left = bisect_left(self.m_array, self.m_target)
        right = bisect_right(self.m_array, self.m_target)
        if right == left : 
            return -1
        return right - left

    def UseBiSearch(self) -> int:
        left = 0
        right = self.m_arrayLen - 1
        findIdx = -1
        while left < right:
            mid = (left + right) // 2
            if self.m_array[mid] == self.m_target:
                findIdx = mid
                break
            elif self.m_array[mid] > self.m_target:
                right = mid -1
            else:
                left = mid + 1
        
        if findIdx == -1:
            return -1

        leftPtr = findIdx - 1
        rightPtr = findIdx + 1
        total = 1
        while leftPtr >= 0:
            if self.m_array[leftPtr] == self.m_target:
                total += 1
                leftPtr -= 1
            else:
                break
        while rightPtr < self.m_arrayLen:
            if self.m_array[rightPtr] == self.m_target:
                total += 1
                rightPtr += 1
            else :
                break
        return total


con = CountOfNum(N, array, x)
print(con.UseBisect())
print(con.UseBiSearch())