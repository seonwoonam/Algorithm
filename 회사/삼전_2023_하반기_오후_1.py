# 3:36
# 1번부터 P번까지 P명의 산타

# 1. 게임판의 구성
# 게임판은 N*N 크기의 격자로 이루어져 있다. v
# 좌상단 (1,1)  v
# 0,0으로 바꿔줘야 함. v
# 게임은 총 M개의 턴 v
# 매턴마다 루돌프와 산타들이 한 번씩 움직임
# 루돌프 먼저 움직이고, 1번 산타부터 P번 산타까지 순서대로 움직임.
# 기절 혹은 격자 밖으로 빠져나간 산타는 움직일 수 없음(탈락)
# 거리 : 제곱합 v

# 2. 루돌프의 움직임
# 가장 가까운 산타를 향해 1칸 돌진(게임에서 탈락하지 않은 산타 중)
# 가까운 산타가 2명이상이면 r좌표가 큰 산타, 이것도 같으면 c좌표가 큰 산타
# 루돌프는 상하좌우, 대각선중 8방향 중 하나로 돌진 가능
# 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 칸 으로 돌진

# 3. 산타의 움직임
# 산타는 1번부터 P번까지 순서대로 움직임(먼저 움직인 것도 바로 반영하겠다는 뜻)
# 기절했거나 이미 탈락한 산타는 못 움직임
# 산타도 루돌프에게 거리가 가장 가까워지는 방향으로
# 다른 산타가 있는 칸이나 게임판 밖으로는 못 움직임
# 움직일 수 있는 칸이 없다면 산타는 안 움직임
# 움직일 수 있는 칸이 있더라도 루돌프로부터 가까워지는 방법이 아니라면 움직이지 않음
# 산타는 상우하좌 움직일 수 있음.

# 4. 충돌
# 루돌프가 움직여서 충돌이 일어난 경우, 산타는 C만큼의 점수를 얻음
# 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려나게 됨
# 산타가 움직여서 충돌이 일어난 경우 산타는 D만큼 점수를 얻음
# 자신이 이동해온 반대방향으로 D칸 만큼 밀려남
# 밀려나는 거는 정확히 원하는 위치에 도달됨
# 밀려난 위치가 게임판 밖이면 산타는 게임에서 탈락
# 밀려난 칸에 다른 산타가 있으면 상호작용

# 5. 상호작용
# 루돌프와 충돌 후에만 상호작용 발생가능
# 산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려남. 연쇄적으로
# 해당 방향 (산타가 밀린 방향)

# 6. 기절
# 산타는 루돌프와 충돌 후 이번턴 다음턴 기절하게됨.
# 기절한 산타는 못움직임.
# 기절 중첩 가능?

# 7. 게임종료
# M번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료
# 만약 P명의 산타가 모두 탈락하면 게임 종료
# 매턴 이후 탈락하지 않은 산타들에게 1점씩 추가로 부여

# 출력
# 게임이 끝났을 때 각 산타가 얻은 최종 점수 구하기
from collections import deque

N, M, P, C, D = map(int, input().split())
RUDOLP = 1000
ru_r, ru_c = map(int, input().split())
ru_r = ru_r - 1
ru_c = ru_c - 1
# -1 빈곳, 각종 인덱스 산타, 1000 루돌프
santa_map = [
    [-1] * N
    for _ in range(N)
]
santa_list = [()] * P
santa_score = [0] * P
santa_alive = [True] * P
santa_gizel = [-1] * P
for _ in range(P):
    idx, r, c = map(int, input().split())
    idx = idx - 1
    r = r - 1
    c = c - 1
    santa_map[r][c] = idx
    santa_list[idx] = (r, c)

santa_map[ru_r][ru_c] = RUDOLP

def calculate_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


# 상, 하, 좌, 우, 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래
rudolp_dr = [-1, 1, 0, 0, -1, -1, 1, 1]
rudolp_dc = [0, 0, -1, 1, -1, 1, -1, 1]
# 상우하좌
santa_dr = [-1, 0, 1, 0]
santa_dc = [0, 1, 0, -1]


def ru_crash(new_row, new_col, direction, now_turn):
    # 테스트 필요
    global santa_map
    global santa_score

    if santa_map[new_row][new_col] != -1 and santa_map[new_row][new_col] != RUDOLP:
        que = deque([])
        santa_idx = santa_map[new_row][new_col]
        santa_map[new_row][new_col] = RUDOLP
        santa_score[santa_idx] += C
        # 기절
        santa_gizel[santa_idx] = now_turn + 1

        next_row = new_row + C * rudolp_dr[direction]
        next_col = new_col + C * rudolp_dc[direction]

        if in_range(next_row, next_col):
            if santa_map[next_row][next_col] != -1:
                que.append((next_row, next_col, santa_idx))
            else:
                santa_map[next_row][next_col] = santa_idx
                santa_list[santa_idx] = (next_row, next_col)
        else:
            santa_alive[santa_idx] = False

        # 상호작용
        while que:
            row, col, state = que.popleft()
            santa_idx = santa_map[row][col]
            santa_map[row][col] = state
            santa_list[state] = (row, col)

            next_row = row + rudolp_dr[direction]
            next_col = col + rudolp_dc[direction]

            if in_range(next_row, next_col):
                if santa_map[next_row][next_col] != -1:
                    que.append((next_row, next_col, santa_idx))
                else:
                    santa_map[next_row][next_col] = santa_idx
                    santa_list[santa_idx] = (next_row, next_col)
            else:
                santa_alive[santa_idx] = False
    else:
        santa_map[new_row][new_col] = RUDOLP


def santa_crash(new_row, new_col, direction, now_turn, idx):
    global santa_map
    global santa_score
    santa_idx = idx
    if santa_map[new_row][new_col] == RUDOLP:
        que = deque([])
        santa_map[new_row][new_col] = RUDOLP
        santa_score[santa_idx] += D
        # 기절
        santa_gizel[santa_idx] = now_turn + 1

        next_row = new_row - D * santa_dr[direction]
        next_col = new_col - D * santa_dc[direction]

        if in_range(next_row, next_col):
            if santa_map[next_row][next_col] != -1:
                que.append((next_row, next_col, santa_idx))
            else:
                santa_map[next_row][next_col] = santa_idx
                santa_list[santa_idx] = (next_row, next_col)
        else:
            santa_alive[santa_idx] = False

        # 상호작용
        while que:
            row, col, state = que.popleft()
            santa_idx = santa_map[row][col]
            santa_map[row][col] = state
            santa_list[state] = (row, col)

            next_row = row - santa_dr[direction]
            next_col = col - santa_dc[direction]

            if in_range(next_row, next_col):
                if santa_map[next_row][next_col] != -1:
                    que.append((next_row, next_col, santa_idx))
                else:
                    santa_map[next_row][next_col] = santa_idx
                    santa_list[santa_idx] = (next_row, next_col)
            else:
                santa_alive[santa_idx] = False
    else:
        santa_map[new_row][new_col] = santa_idx
        santa_list[santa_idx] = (new_row, new_col)


for turn in range(M):
    # === 루돌프 움직이기 =====
    now_close = 10000
    selected_santa_list = []
    for i in range(N):
        for j in range(N):
            if santa_map[i][j] != -1 and santa_map[i][j] != RUDOLP:
                distance = calculate_distance(ru_r, ru_c, i, j)
                if now_close > distance:
                    now_close = distance
                    selected_santa_list = [(i, j)]
                elif now_close == distance:
                    selected_santa_list.append((i, j))

    selected_santa_list.sort(key=lambda x: (-x[0], -x[1]))
    selected_santa = selected_santa_list[0]

    now_distance = 10000
    next_ru_pos = (-1, -1)
    direction = -1
    for i in range(8):
        next_ru_r = ru_r + rudolp_dr[i]
        next_ru_c = ru_c + rudolp_dc[i]

        if in_range(next_ru_r, next_ru_c):
            distance = calculate_distance(selected_santa[0], selected_santa[1], next_ru_r, next_ru_c)
            if distance < now_distance:
                direction = i
                now_distance = distance
                next_ru_pos = (next_ru_r, next_ru_c)
    santa_map[ru_r][ru_c] = -1
    ru_r = next_ru_pos[0]
    ru_c = next_ru_pos[1]

    # 충돌 계산
    ru_crash(ru_r, ru_c, direction, turn)

    for idx in range(len(santa_list)):
        santa_r = santa_list[idx][0]
        santa_c = santa_list[idx][1]

        if santa_alive[idx] == False or santa_gizel[idx] >= turn:
            continue

        now_distance = calculate_distance(ru_r, ru_c, santa_r, santa_c)
        next_san_pos = (-1,-1)
        direction = -1

        for k in range(4):
            next_r = santa_r + santa_dr[k]
            next_c = santa_c + santa_dc[k]

            if in_range(next_r, next_c) :
                distance = calculate_distance(ru_r, ru_c, next_r, next_c)
                if distance >= now_distance:
                    continue

                if santa_map[next_r][next_c] == -1 :
                    direction = k
                    next_san_pos = (next_r, next_c)
                    now_distance = distance
                elif santa_map[next_r][next_c] == RUDOLP:
                    direction = k
                    next_san_pos = (next_r, next_c)
                    now_distance = 0
                    break
        if next_san_pos == (-1,-1):
            continue

        santa_map[santa_r][santa_c] = -1
        # 충돌 판단
        santa_crash(next_san_pos[0],next_san_pos[1],direction, turn, idx)

    next_turn = False
    for i in range(P):
        if santa_alive[i] :
            next_turn = True
            santa_score[i] += 1
    if next_turn == False :
        break


for i in range(P):
    print(santa_score[i], end=" ")
