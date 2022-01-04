# 문제: 주어진 두 string s와 t가 isomorphic 관계인지 찾아서 return하여라

def IsIsomorphic(strA : str, strB : str) -> bool:
    hashMap = {}

    if len(strA) != len(strB):
        return False
    
    for idx in range(0,len(strA)):
        if not strA[idx] in hashMap:
            hashMap[strA[idx]] = strB[idx]
        else:
            if strB[idx] == hashMap[strA[idx]]:
                continue
            else:
                return False

    return True


print(IsIsomorphic(strA="aaaccd", strB="xxxyyz"))
print(IsIsomorphic(strA="aaaccd", strB="xcxyyz"))