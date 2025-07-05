# 백준 1043
# 사람의 수 : N
# 이야기의 진실을 아는 사람이 주어짐
# 각 파티에 오는 사람들의 번호가 주어짐.

# 진실을 아는 사람이 왔을 때는 -> 진실
# 어떤 파티에서 진실 + 다른 파티에서 과장 -> 안됨

# 출력
# 모든 파티에 참가. 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티의 개수
# 최댓값

# N,M <= 50
# 파티 사람 <= 50

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
first = list(map(int, sys.stdin.readline().rstrip().split()))
true_known_list = set(first[1:])
party_list = []
for i in range(M):
    people_list = list(map(int, sys.stdin.readline().rstrip().split()))
    party_list.append(set(people_list[1:]))

can_lie = [True] * (M)

que = deque(list(true_known_list))

while que:
    now_true_know_person = que.popleft()
    for i in range(M):
        if can_lie[i] == True:
            if not now_true_know_person in party_list[i]:
                continue
            can_lie[i] = False
            for people in party_list[i]:
                if not people in true_known_list:
                    que.append(people)
                    true_known_list.add(people)

result = 0 
for i in range(M):
    if can_lie[i] :
        result += 1
print(result)