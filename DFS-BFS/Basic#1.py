# 유클리드 호제법을 이용하여 두 개의 자연수에 대한 최대 공약수를 구하라
# 유클리드 호제법
# 두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지를 R이라고 하면
# A, B의 최대 공약수는 B와 R의 최대 공약수와 같다.

def GCD(a :int, b: int) -> int:
    if a%b == 0: 
        return b
    else:
        return GCD(b, a%b)

print(GCD(192,162))