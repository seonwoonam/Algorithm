# 9935
# 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열 합쳐짐
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을수도 있다.
# 폭발은 폭발 문자열이 없을 때까지 계속된다.

# 출력
# 모든 폭발이 끝난 후에 어떤 문자열이 남는지?
# 남아있는 문자가 없을 때는 FRULA 출력

# 기타
# 폭발 문자열은 같은 문자를 2개이상 포함하지 않음

# N <= 10^6
# N

# 그냥 stack으로 풀기?

import sys
from collections import deque

arr = sys.stdin.readline().rstrip()
bomb_str = sys.stdin.readline().rstrip()

que = deque()

for i in range(len(arr)):
    que.append(arr[i])

    find = True
    for j in range(1,len(bomb_str)+1):
        length = len(que)

        if length - j < 0:
            find = False
            break

        if que[length-j] == bomb_str[len(bomb_str)-j]:
            continue
        else :
            find = False
            break

    if find :
        for _ in range(len(bomb_str)):
            que.pop()

if len(que) == 0:
    print("FRULA")
else :  
    print("".join(que))