# 한 변의 길이가 N인 2차원 평면
# 그 사이 어디엔가 한 변의 길이가 M인 정육면체

# 타임머신은 빈 공간만 이동 가능 : 빈공간 0, 장애물 1
# 타임머신은 시간의 벽 윗면 어딘가에 위치 : 2

# 시간의 벽과 미지의 공간의 바닥으로 이어질 수 있는 출구는 하나

# 시간의 벽의 위치 3과 탈출구 4

# 미지의 공간 바닥에는 총 F개의 시간 이상 현상
# 시간 이상 현상은 장애물과 탈출구가 없는 빈 공간으로만 확산

# 타임머신이 장애물과 시간 이상 현상을 피해 탈출구까지 도달해야함

# 출력
# 타임머신이 시작점에서 탈출구까지 이동하는데 필요한 최소 시간
# 최소 턴수 구하기
# 없다면 -1 출력

import sys
from collections import deque

N, M, F = map(int, sys.stdin.readline().rstrip().split())
# 미지의 공간
miji = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(N)
]

miji_id = [
    [-1] * N
    for _ in range(N)
]

# 시간의 벽 : 동남서북 + 윗면
time_wall = [
    []
    for _ in range(5)
]
direction = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
time_wall[0] = direction
direction = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
time_wall[2] = direction
direction = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
time_wall[1] = direction
direction = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
time_wall[3] = direction
direction = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(M)
]
time_wall[4] = direction

time_wall_id = [
    [[-1] * M
    for _ in range(M)]
    for _ in range(5)
]

# 시간 이상
time_isang = []
for _ in range(F):
    isang = list(map(int, sys.stdin.readline().rstrip().split()))
    time_isang.append(isang)

# 기타 필요한 것들
# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def in_range_miji(x, y):
    return 0 <= x < N and 0 <= y < N


def in_range_time(x, y):
    return 0 <= x < M and 0 <= y < M


def change_index(x):
    if x >= M:
        return x % M
    elif x < 0:
        return x + M
    else:
        return x


# ======================== 그래프로 만들기 =================================
# id 주기
cnt = 0
for i in range(N):
    for j in range(N):
        if miji[i][j] != 3 :
            miji_id[i][j] = cnt
            cnt += 1

for k in range(5):
    for i in range(M):
        for j in range(M):
            time_wall_id[k][i][j] = cnt
            cnt += 1

graph = [
    []
    for _ in range(cnt)
]

# 미지 이어주기
for i in range(N):
    for j in range(N):
        if miji[i][j] != 3 :
            for k in range(4):
                next_i = i + dx[k]
                next_j = j + dy[k]

                if in_range_miji(next_i, next_j) and miji[next_i][next_j] != 3:
                    idx = miji_id[i][j]
                    next_idx = miji_id[next_i][next_j]
                    graph[idx].append(next_idx)

# 시간의 벽 이어주기
for t in range(5):
    for i in range(M):
        for j in range(M):
            for k in range(4):
                next_i = i + dx[k]
                next_j = j + dy[k]

                if in_range_time(next_i, next_j):
                    idx = time_wall_id[t][i][j]
                    next_idx = time_wall_id[t][next_i][next_j]
                    graph[idx].append(next_idx)

# 시간의 벽끼리 이어주기 : 옆면들
# 동남서북
# 0123

for t in range(4):
    for i in range(M):
        for j in range(M):
            for k in [0,2]:
                next_i = i + dx[k]
                next_j = j + dy[k]

                if next_i >= M or next_i < 0 :
                    continue

                if next_j >= M :
                    idx = time_wall_id[t][i][j]
                    next_idx = time_wall_id[(t-1)%4][next_i][0]
                    graph[idx].append(next_idx)
                elif next_j < 0 :
                    idx = time_wall_id[t][i][j]
                    next_idx = time_wall_id[(t+1)%4][next_i][M-1]
                    graph[idx].append(next_idx)

# 동남서북
# 0123
# 시간의 벽끼리 이어주기 : 윗면에서 옆면들로
for i in range(M):
    for j in range(M):
        for k in range(4):
            next_i = i + dx[k]
            next_j = j + dy[k]

            idx = time_wall_id[4][i][j]
            if k == 0 and not in_range_time(next_i, next_j):
                next_idx = time_wall_id[0][0][(M-1-i)]
                graph[idx].append(next_idx)
                graph[next_idx].append(idx)
            elif k == 1 and not in_range_time(next_i, next_j) :
                next_idx = time_wall_id[1][0][j]
                graph[idx].append(next_idx)
                graph[next_idx].append(idx)
            elif k == 2  and not in_range_time(next_i, next_j):
                next_idx = time_wall_id[2][0][i]
                graph[idx].append(next_idx)
                graph[next_idx].append(idx)
            elif k == 3  and not in_range_time(next_i, next_j):
                next_idx = time_wall_id[3][0][(M-1-j)]
                graph[idx].append(next_idx)
                graph[next_idx].append(idx)

# 시간의 벽과 미지 이어지는 부분 연결
start_time_i = -1
start_time_j = -1
for i in range(N):
    for j in range(N):
        if miji[i][j] == 3 :
            start_time_i = i
            start_time_j = j
            break
    if start_time_i != -1:
        break

find_1 = False
for i in range(start_time_i, start_time_i+M):
    for j in range(start_time_j, start_time_j+M):
        for k in range(4):
            next_i = i + dx[k]
            next_j = j + dy[k]

            if in_range_miji(next_i, next_j) and miji[next_i][next_j] == 0:
                idx = miji_id[next_i][next_j]

                if k == 3 :
                    # 위쪽에서 발견(북)
                    next_idx = time_wall_id[3][M-1][(M - 1 - (j- start_time_j)) % M]
                    graph[next_idx].append(idx)
                elif k == 2 :
                    # 왼쪽에서 발견(서)
                    next_idx = time_wall_id[2][M-1][i-start_time_i]
                    graph[next_idx].append(idx)
                elif k == 1 :
                    # 아래쪽에서 발견(남)
                    next_idx = time_wall_id[1][M-1][j-start_time_j]
                    graph[next_idx].append(idx)
                elif k == 0 :
                    # 오른쪽에서 발견(동)
                    next_idx = time_wall_id[0][M-1][(M - 1 - (i- start_time_i)) % M]
                    graph[next_idx].append(idx)

                find_1 = True
                break
        if find_1 :
            break
    if find_1 :
        break


# 시작 위치 찾기
start_idx = -1
for i in range(M):
    for j in range(M):
        if time_wall[4][i][j] == 2:
            start_x = i
            start_y = j

            start_idx = time_wall_id[4][start_x][start_y]
            break

# 도착지 찾기
end_idx = -1
for i in range(N):
    for j in range(N):
        if miji[i][j] == 4 :
            end_idx = miji_id[i][j]
            break

# 못 가는 지역 막기
visited = [False] * cnt
for i in range(N):
    for j in range(N):
        if miji[i][j] == 1:
            idx = miji_id[i][j]
            visited[idx] = True

for t in range(5):
    for i in range(M):
        for j in range(M):
            if time_wall[t][i][j] == 1:
                idx = time_wall_id[t][i][j]
                visited[idx] = True

def bfs(st_idx):
    global visited
    que = deque([])

    visited[st_idx] = True
    que.append((0, st_idx))

    while que :
        turn, idx = que.popleft()

        # 시간 이상현상 처리
        time_strange = [False] * cnt
        for isang in time_isang:
            isang_x = isang[0]
            isang_y = isang[1]
            direction = isang[2]
            constant = isang[3]

            if direction == 1 :
                direction = 2
            elif direction == 2 :
                direction = 1

            for i in range((turn // constant) + 1):
                next_x = isang_x + i * dx[direction]
                next_y = isang_y + i * dy[direction]

                if in_range_miji(next_x, next_y) and miji[next_x][next_y] == 0 :
                    isang_idx = miji_id[next_x][next_y]
                    time_strange[isang_idx] = True


        if idx == end_idx :

            return turn

        for next_idx in graph[idx]:
            if not visited[next_idx] and not time_strange[next_idx]:
                visited[next_idx] = True
                que.append((turn + 1, next_idx))

    return -1

print(bfs(start_idx))
