# 미로 탈출
# 0 -> 1
# 수평이나 수직으로 한칸 이동

# 이동 횟수의 최솟값 구하기
# N, M <= 50

# 탈출 못하면 -1
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [
    sys.stdin.readline().rstrip()
    for _ in range(N)
]

# BFS, DP, 다익스트라

# 가는 길에 열쇠가 있는지 없는지 모른다.
# BFS 갈 수 있는한 최대한 가보기

# 무언가를 얻으면 한번더
# 무언가를 얻지 못하면 끝

# 내가 생각했던 방식은 열쇠 얻고 난 뒤 다시 BFS 호출
# 답에서는 비트마스킹과 3차원 visited를 이용해서 다시 Queue를 돌리는 방식으로 구현하는듯.
# 3차원으로 하는 이유는 키를 갖고 다시 방문했을 때는 다르다!


for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            start_x = i 
            start_y = j

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

def BFS(start_x, start_y):
    que = deque()
    visited = [[
        [False] * (1 << 6)
        for _ in range(M)]
        for _ in range(N)
    ]

    # x,y,depth, key
    que.append((start_x,start_y,0,0))
    visited[start_x][start_y][0] = True

    while que:
        now_x, now_y, depth, key = que.popleft()

        if arr[now_x][now_y] == '1' :
            return depth
        
        if arr[now_x][now_y] in {'a', 'b', 'c', 'd', 'e', 'f'}:
            key = key | (1 << ord(arr[now_x][now_y])-ord('a'))

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            if in_range(next_x, next_y) and visited[next_x][next_y][key] != True and arr[next_x][next_y] != '#':
                if arr[next_x][next_y] in {'A', 'B', 'C', 'D', 'E', 'F'}:
                    if key & ( 1 << ord(arr[next_x][next_y]) - ord('A')) :
                        que.append((next_x, next_y, depth + 1, key))
                        visited[next_x][next_y][key] = True
                else:
                    que.append((next_x, next_y, depth + 1, key))
                    visited[next_x][next_y][key] = True

                
    return -1

print(BFS(start_x, start_y))


# 64 32 16 8 4 2 1
#     f e  d c   b  a
# 64까지 넣을 수 있게 해야한다. 111111 때문에