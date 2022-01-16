from bisect import bisect_left


class BinarySearch:
    def __init__(self, array) -> None:
        self.m_array = array

    # 재귀적으로 구현
    def SearchRecur(self, target : int) ->int:
        return self._searchRecur(target, 0, len(self.m_array) - 1)

    def _searchRecur(self, target : int, left : int, right : int) -> int:
        if left > right :
            return None
        
        middle = (right + left ) // 2
        if self.m_array[middle] == target :
            return middle
        elif self.m_array[middle] > target:
            return self._searchRecur(target, left, middle - 1)
        else :
            return self._searchRecur(target, middle + 1, right)       


    # while로 구현
    def SearchWhile(self, target : int) ->int:
        left = 0
        right = len(self.m_array) - 1
        while (left < right):
            mid = (left + right) // 2
            if self.m_array[mid] == target:
                return mid
            elif self.m_array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

n, target  = list(map(int, input().split()))
g_array = list(map(int, input().split()))

bs = BinarySearch(g_array)
print(bs.SearchRecur(target))
print(bs.SearchWhile(target))


from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
print(bisect_left(a, 4))
print(bisect_right(a, 4))
