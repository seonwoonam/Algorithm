"""
    N comb R 값을 1234567891로 나눈 나머지
    N <= 1,000,000

    숫자크기가 감당이 되나??
    그냥 곱하면 안될듯.

    나머지를 분배법칙으로 적용시켜야 하는데
    나누기에는 분배법칙이 적용되지 않는다. 그래서 페르마의 소정리를 통해 곱하기로 변경하고
    분배법칙을 적용해야 한다. 

    구현 진행
    분배법칙 적용했다 치고 분모, 분자 계산
    페르마의 소정리 적용시켜서 곱셈으로 바꾼 후 계산
    제곱 계산은 분할정복으로
"""

def div_pow(a, s, mod):
    if s == 1:
        return a
    
    temp = div_pow(a, s // 2, mod)
    if s % 2 == 1:
        # 홀수
        return ((temp * temp) % mod * a) % mod
    else : 
        # 짝수
        return (temp * temp) % mod

T = int(input())
for test_case in range(1, T + 1):
    N, R = map(int, input().split())
    parent = 1
    child = 1
    mod = 1234567891

    for i in range(N, N-R, -1):
        child = (child * i) % mod 
    
    for i in range(R, 1, -1):
        parent = (parent * i) % mod
    
    result = (child * div_pow(parent, mod-2, mod)) % mod 
    print('#{} {}'.format(test_case, result))

    
