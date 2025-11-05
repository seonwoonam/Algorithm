# 빌런 호석
"""
    11:23
    1층부터 N층까지 이용이 가능한 엘리베이터. 

    엘레베이터의 층수를 보여주는 디스플레이에는 K 자리의 수가 보인다.
    수는 0으로 시작할 수도 있다. 

    K=4일때 501층은 0501 으로 보인다. 

    LED 중에서 최소 1개, 최대 P개를 반전시킬 계획을 세우고 있다. 

    또한 반전 이후에 디스플레이가 올바른 수가 보여지면서 1이상 N이하가 되도록 바꿔서 사람들을 헷갈리게 할 예정.
    호석 빌런의 행동을 미리 파악해서 혼쭐. 현재 엘레이테이터가 실제로는 X층에 멈춰있을 때, 호석이가 반전시킬 LED를 고를 수 있는 경우의 수를 계산

    1<X<10^6
    1<K<6
    1<P<42

    바꿀 수 있는 LED 개수 계산 


    각 숫자에서 다른 숫자로 몇개써서 변환시킬 수 있는지 확인. 
        - 9+8+7+6+5+4+3+2+1 = 45
    그거에 대한 합이 42가 되는 수의 개수?

    그래프, 구현, 탐색, 유니온, 그리디, 투포인터, 디피, 투포인터, 완탐......
"""




N, K, P, X = input().split()
result = 0

check_list = [''] * 10

check_list[0] = '1111110'
check_list[1] = '0000110'
check_list[2] = '1011011'
check_list[3] = '1001111'
check_list[4] = '0100111'
check_list[5] = '1101101'
check_list[6] = '1111101'
check_list[7] = '1000110'
check_list[8] = '1111111'
check_list[9] = '1101111'

result = set()

def backtracking(now_count, now_index, num_str) :
    global P
    global check_list
    global result

    if(now_index != -1) : 
        if 1 <= int(num_str) <= int(N) and now_count <= int(P) and now_index < int(K) :
            result.add(num_str)
        elif 1 <= int(num_str) <= int(N) and now_count <= int(P) and now_index == int(K):
            result.add(num_str)
            return
        elif now_index >= int(K) or now_count > int(P) :
            return 
    else :
        now_index = 0
    
    now_num = int(num_str[now_index])
    for i in range(10):
        if i == now_num :
            continue 

        count = 0
        for j in range(7):
            if check_list[i][j] != check_list[now_num][j]:
                count += 1
        
        new_str = num_str[0:now_index] + str(i) + num_str[now_index+1:]
        backtracking(now_count +count, now_index + 1, new_str)

num_str = X
for i in range(int(K) - len(X)):
    num_str = '0' + num_str


backtracking(0, -1, num_str)
print(len(result))
