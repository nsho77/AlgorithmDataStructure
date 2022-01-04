# 문제: 주어진 String s에서 반복되지 않는 첫번째 character의 index를 return하여라

def FindFirstUniqueCharacter(stringParam : str) -> int:
    hashMap = {}
    for c in stringParam:
        if c in hashMap:
            hashMap[c] += 1
        else:
            hashMap[c] = 1

    for idx, c in enumerate(stringParam):
        if hashMap[c] == 1:
            return idx

    return -1

print(FindFirstUniqueCharacter("nocodeprogram"))
print(FindFirstUniqueCharacter("nownocodeprogram"))