# 게임종료
# 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝
# 게임끝나는데 걸리는 최소시간은?

# 코니
# 처음위치 C에서 1초후 1만큼 움직이고, 이후에는 가속이 붙어 매 초마다 이전 이동거리 +1 

# 브라운
# 현재 위치 B에서 다음 순간 B-1, B+1, 2*B 중 하나로 움직일 수 있다.

# 위치 조건은 <= 200,000

# 코니가 범위를 벗어나면 게임이 끝나게됨

# 출력
# 브라운이 코니를 잡는 최소시간 N 출력, 못잡으면 -1 출력
# import sys 
# C, B = map(int, sys.stdin.readline().rstrip().split())

# 그리디
# now_time = 0
# move = 0
# find = False
# while C <= 200000:
#     if C == B:
#         print(now_time)
#         break
#     else:
#         temp_C = C
#         for i in range(now_time):
#             if temp_C - 1 == B:
#                 temp_C = temp_C - 1
#             elif temp_C + 1 == B:
#                 temp_C = temp_C + 1
#             elif temp_C / 2 == B :
#                 temp_C = temp_C / 2
#             elif temp_C % 2 == 0:
#                 temp_C = temp_C / 2
#             elif temp_C % 2 == 1:
#                 if temp_C - B > 0:
#                     temp_C = temp_C - 1
#                 else :
#                     temp_C = temp_C + 1

#         if temp_C == B:
#             print(now_time)
#             break

#         move = move + 1
#         C = C + move
#         now_time += 1



import sys 
from collections import deque
C, B = map(int, sys.stdin.readline().rstrip().split())
MAX = 200000

if C == B:
    print(0)
else :
    que = deque([])
    visited = [
        [False] * [MAX+1]
        for _ in range(2)
    ]
    visited[0][B] = True
    t = 0

    while True:
        connie = C + t*(t+1) // 2
        if connie > MAX :
            print(-1)
            break
        

# 어떻게 bfs를
# 짝,홀수 개념이 왜 나옴?
# 홀짝이 없으면 