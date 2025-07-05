# N*N개의 방이 있는 헛간
# 최대한 많은 방에 불 밝히기

# 어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치 존재
# 불이 켜져있는 방으로만 들어갈 수 있고, 각 방에서는 상하좌우에 인접한 방으로 움직일 수 있다.

# 출력
# 불을 켤 수 있는 방의 최대 개수 구하기

# N <= 100
# M <= 20000
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())

# bfs + 생각을 더 했으면 되는 문제
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def in_range(r,c):
    return 0<=r<N and 0<=c<N
light_list = [
    [set()
     for _ in range(N)] 
    for _ in range(N)
] 
for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    a -= 1
    b -= 1
    light_list[x][y].add((a,b))
turn_light = [
    [False] * N
    for _ in range(N)
]
turn_light[0][0] = True
visited = [
    [False] * N 
    for _ in range(N)
]

result = 1
que = deque([])
que.append((0,0))
visited[0][0] = True

while que :
    r, c = que.popleft()

    for light in light_list[r][c]:
        if turn_light[light[0]][light[1]] == False:
            result += 1
        turn_light[light[0]][light[1]] = True

        can_enter = False
        for k in range(4):
            next_r = light[0] + dr[k]
            next_c = light[1] + dc[k]

            if in_range(next_r, next_c) and visited[next_r][next_c] == True:
                can_enter = True
        
        if can_enter and visited[light[0]][light[1]] == False:
            que.append((light[0],light[1]))
            visited[light[0]][light[1]] = True


    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]

        if in_range(next_r, next_c) and visited[next_r][next_c] == False and turn_light[next_r][next_c]:
            visited[next_r][next_c] = True
            que.append((next_r, next_c))


print(result)