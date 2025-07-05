#8980
# 마을에 있는 물건을 배송
# 각 마을은 배송할 물건들을 박스에 넣어보낸다.
# 트럭에 최대로 실을 수 있는 박스 개수 있음

# 조건
# 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 트럭은 지나온 마을로 되돌아가지 않는다.
# 박스들 중 일부만 배송 가능하다.
# 받는 마을번호는 보내는 마을번호보다 항상 크다.

# 출력
# 트럭 한 대로 배송할 수 있는 최대 박스 수 구하기

# N <= 2,000
# C <= 10,000
# M <= 10,000

# 생각
# 많이 배송하기 위해서는 중간에 많이 내려야한다.
# 다음수를 생각해야함.

# 유형
# 그리디. 자기보다 뒤에 가는데, 공간이 없으면 버리게

import sys
from collections import deque
N, C = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
delivery_list = []
graph = [
    dict()
    for _ in range(N)
]
for _ in range(M):
    S, R, T = map(int, sys.stdin.readline().rstrip().split())
    delivery_list.append((S-1,R-1,T))
    graph[S-1][R-1] = T
delivery_list.sort(key=lambda x : (x[0], x[1]))
NOW_C = 0
# 목적지 : Cost
now_delivery = dict()
result = 0
for i in range(N):
    now_delivery[i] = 0

for delivery in delivery_list:
    send, receive, cost = delivery
    result += now_delivery[send]
    NOW_C -= now_delivery[send]
    now_delivery[send] = 0

    for i in range(send):
        if now_delivery[i] > 0:
            result += now_delivery[i]
            NOW_C -= now_delivery[i]
            now_delivery[i] = 0

    # 일단 다 적재
    NOW_C += cost
    now_delivery[receive] += cost

    # 공간 초과하면 뒤에서부터 빼주기
    if NOW_C > C:
        remove = NOW_C - C
        for i in range(N-1,-1,-1):
            if remove == 0:
                break
            if now_delivery[i] == 0:
                continue
            if now_delivery[i] < remove :
                remove -= now_delivery[i]
                now_delivery[i] = 0
            else :
                now_delivery[i] -= remove
                remove = 0
        NOW_C = C
                
result += NOW_C
print(result)