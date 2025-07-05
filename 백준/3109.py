# 빵집이 있는 곳은 R*C 격자로 표현 가능
# 첫번째 열 : 근처 빵집의 가스관
# 마지막 열 : 빵집
# 건물이 있는 경우 파이프 x

# 오른쪽, 오른쪽 위 대각선, 아래 대각 선
# 여러개 설치하는데 겹치거나 접하면 안됨

# 파이프라인 최대 개수

# R <= 10000
# C <= 500

# dfs로 안겹치게 그냥 보내기

import sys
sys.setrecursionlimit(10**8)
R, C = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(R):
    arr.append(sys.stdin.readline().rstrip())

dx = [-1, 0, 1]
dy = [1, 1, 1]


def in_range(x, y):
    return 0<=x<R and 0<=y<C

visited = [
    [False] * C 
    for _ in range(R)
]

result = 0

def DFS(start_x, start_y, depth):
    global result
    global visited 

    visited[start_x][start_y] = True 
    
    if depth == C:
        result += 1
        return True
    
    for k in range(3):
        next_x = start_x + dx[k]
        next_y = start_y + dy[k]

        if in_range(next_x, next_y) and arr[next_x][next_y] != 'x' and visited[next_x][next_y] != True:
            check = DFS(next_x, next_y, depth+1)
            if check :
                return True

    return False

for i in range(R):
    DFS(i,0,1)

print(result)