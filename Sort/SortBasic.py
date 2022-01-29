from typing import List
# 선택 정렬
def SelectionSort(arr: List[int]) -> None:
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i] # 스와프

    print(arr)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
SelectionSort(array)

# 삽입 정렬
def InsertionSort(arr: List[int]) -> None:
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] # swap
            else:
                break
    print(arr)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
InsertionSort(array)

# 퀵 정렬
def QuickSort(arr: List[int], start: int, end: int) -> None:
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = Partition(arr, start, end)

    QuickSort(arr, start, pivot - 1)
    QuickSort(arr, pivot + 1, end)

def Partition(arr: List[int], start: int, end: int) -> int:
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
            pivot = right
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return pivot

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
QuickSort(array, 0, len(array)-1)
print(array)

# 계수 정렬
def RedixSort(arr: List[int]) -> None:
    # 모든 원소의 값이 0보다 크거나 같다고 가정
    # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
    count = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=" ") #등장한 횟수만큼 인덱스 출력

array = [7, 4, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
RedixSort(array)
