# 3:30

# 0. 포탑 정보
# N * M 격자 : 모든 위치에 포탑 존재 v
# 포탑 공격력 있는데 줄어들거나, 늘어나거나 할 수 있음 v
# 공격력 0이하 되면, 포탑은 부서지며 공격 못함 v

# 0-1. K번 반복. 액션
# 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지. v

# 1. 공격자 선정
# 가장 약한 포탑이 공격자로 선정됨
# 가장 약한 포탑은 공격력이 가장 낮은 v
# 만약 2개면, 가장 최근에 공격한 포탑(모든 포탑은 시점0에서 모두 공격한 경험이 있음) v
# ++ 그러한 포탑이 2개이상이면, 행과 열의 합이 가장 큰 포탑 v
# ++ 그러한 포탑이 2개이상이면, 열 값이 가장 큰 포탑 v
# 핸디캡 : N+M 만큼의 공격력이 증가됨 v

# 2. 공격자의 공격
# 자신을 제외한 가장 강한 포탑 공격 v
# 가장 강한 포탑 v
# 공격력이 가장 높은 v
# 만약 2개이상이면, 공격한지 가장 오래된 v
# 2개이상이면, 행과 열의 합이 가장 작은 v
# 2개이상이면, 열의 값이 가장 작은 v

# 레이저 공격 먼저시도, 안되면 포탄 공격
# 3. 레이저 공격
# 상하좌우 4개의 방향 v
# 부서진 포탑이 있는 위치는 지날 수 없음 v
# 가장자리에서 막힌 방향으로 지나가면 반대편으로 v
# 공격자의 위치에서 최단 경로로 공격 v
# 경로 존재하지 않으면 포탄 공격 v
# 최단 경로가 2개 이상이면 -> 우하좌상의 우선순위 v
# 공격자의 공격력만큼 피해 입히며, 피해를 받은 포탑은 공격력 줄어듦 v
# + 레이저 경로에 있는 포탑도 공격을 받음( 공격자 공격력의 절반만큼  공격력 // 2) v

# 4. 포탄 공격
# 공격자의 공격력 만큼 피해받음 v
# 주위 8개의 방향에 있는 포탑도 피해받음. 절반만큼 v
# 공격자는 영향 안받음 v
# 가장자리라면, 추가 피해가 반대편 격자에 미치게 됨 v

# 5. 포탑 부서짐
# 공격을 받아 공격력이 0 이하가 된 포탑 부서짐 v

# 6. 포탑 정비
# 공격과 무관했던 포탑은 공격력이 1씩 올라감 v
# 무관하다는 의미는 공격자도 아니고, 피해입은 포탑도 아님 v

# 출력
# K번의 턴이 종료된 후 남아있는 포탑 중 가장 강한 포탑의 공격력 출력

from collections import deque

N, M, K = map(int, input().split())
potop = [
    list(map(int, input().split()))
    for _ in range(N)
]

potop_attack_time = [
    [0] * M
    for _ in range(N)
]

# 우하좌상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def get_path_bfs(start_i, start_j, end_i, end_j):
    visited = [
        [False] * M
        for _ in range(N)
    ]
    que = deque([])
    que.append(([], start_i, start_j))
    visited[start_i][start_j] = True

    while que:
        path, i, j = que.popleft()
        if i == end_i and j == end_j:
            return path
        for k in range(4):
            next_i = i + di[k]
            next_j = j + dj[k]

            if next_i < 0 or next_i >= N:
                next_i = next_i % N
            elif next_j < 0 or next_j >= M:
                next_j = next_j % M

            if is_available_potop(next_i, next_j):
                if visited[next_i][next_j] != True:
                    que.append((path + [(next_i, next_j)], next_i, next_j))
                    visited[next_i][next_j] = True

    return []


def is_available_potop(i, j):
    if potop[i][j] > 0:
        return True
    else:
        return False


for time in range(K):
    temp_potop = [
        [0] * M
        for _ in range(N)
    ]
    for i in range(N):
        for j in range(M):
            temp_potop[i][j] = potop[i][j]

    # 부서지지 않는 포탑 개수 확인
    not_broken_potop_count = 0
    for i in range(N):
        for j in range(M):
            if is_available_potop(i, j):
                not_broken_potop_count += 1
    if not_broken_potop_count == 1:
        break

    # 공격자 선정
    attacker_list = set()
    min_attack = 50000
    for i in range(N):
        for j in range(M):
            if is_available_potop(i, j):
                if min_attack > potop[i][j]:
                    attacker_list = {(i, j)}
                    min_attack = potop[i][j]
                elif min_attack == potop[i][j]:
                    attacker_list.add((i, j))

    if len(attacker_list) >= 2:
        temp_attacker_list = set()
        recent_attack_time = -1
        for attacker in attacker_list:
            if recent_attack_time < potop_attack_time[attacker[0]][attacker[1]]:
                recent_attack_time = potop_attack_time[attacker[0]][attacker[1]]
                temp_attacker_list = {(attacker[0], attacker[1])}
            elif recent_attack_time == potop_attack_time[attacker[0]][attacker[1]]:
                temp_attacker_list.add(attacker)
        attacker_list = temp_attacker_list

    if len(attacker_list) >= 2:
        sum_i_j = 0
        temp_attacker_list = set()
        for attacker in attacker_list:
            if sum_i_j < (attacker[0] + attacker[1]):
                sum_i_j = (attacker[0] + attacker[1])
                temp_attacker_list = {(attacker[0], attacker[1])}
            elif sum_i_j == (attacker[0] + attacker[1]):
                temp_attacker_list.add(attacker)
        attacker_list = temp_attacker_list

    final_attacker = (-1, -1)
    if len(attacker_list) >= 2:
        colm_max = -1
        for attacker in attacker_list:
            if colm_max < attacker[1]:
                colm_max = attacker[1]
                final_attacker = attacker
    else:
        final_attacker = attacker_list.pop()

    temp_potop[final_attacker[0]][final_attacker[1]] += (N + M)

    # 공격 받는 포탑 선정
    victim_list = set()
    max_attack = 0
    for i in range(N):
        for j in range(M):
            if is_available_potop(i, j) and (i != final_attacker[0] or j != final_attacker[1]):
                if max_attack < potop[i][j]:
                    victim_list = {(i, j)}
                    max_attack = potop[i][j]
                elif max_attack == potop[i][j]:
                    victim_list.add((i, j))

    if len(victim_list) >= 2:
        recent_attack_time = 10000
        temp_victim_list = set()
        for victim in victim_list:
            if recent_attack_time >= potop_attack_time[victim[0]][victim[1]]:
                recent_attack_time = potop_attack_time[victim[0]][victim[1]]
                temp_victim_list = {(victim[0], victim[1])}
            elif recent_attack_time == potop_attack_time[victim[0]][victim[1]]:
                temp_victim_list.add(victim)
        victim_list = temp_victim_list

    if len(victim_list) >= 2:
        sum_i_j = 10000
        temp_victim_list = set()
        for victim in victim_list:
            if sum_i_j >= (victim[0] + victim[1]):
                sum_i_j = (victim[0] + victim[1])
                temp_victim_list = {(victim[0], victim[1])}
            elif sum_i_j == (victim[0] + victim[1]):
                temp_victim_list.add(victim)
        victim_list = temp_victim_list

    final_victim = (-1, -1)
    if len(victim_list) >= 2:
        colm_min = 10000
        for victim in victim_list:
            if colm_min > victim[1]:
                colm_min = victim[1]
                final_victim = victim
    else:
        final_victim = victim_list.pop()

    # 레이저 공격
    path_list = get_path_bfs(final_attacker[0], final_attacker[1], final_victim[0], final_victim[1])
    attack_power = temp_potop[final_attacker[0]][final_attacker[1]]
    if len(path_list) > 0:
        for path in path_list:
            if path[0] == final_victim[0] and path[1] == final_victim[1]:
                temp_potop[path[0]][path[1]] -= attack_power
            else :
                temp_potop[path[0]][path[1]] -= (attack_power//2)
    else :
        temp_potop[final_victim[0]][final_victim[1]] -= attack_power
        dx = [-1,-1,-1,0,0,1,1,1]
        dy = [-1,0,1,-1,1,-1,0,1]
        for k in range(8):
            next_i = dx[k] + final_victim[0]
            next_j = dy[k] + final_victim[1]

            if next_i < 0 or next_i >= N:
                next_i = next_i % N
            if next_j < 0 or next_j >= M:
                next_j = next_j % M

            if is_available_potop(next_i, next_j) and (next_i != final_attacker[0] or next_j != final_attacker[1]):
                temp_potop[next_i][next_j] -= (attack_power//2)

    # 가장 최근 공격 시기 업데이트
    potop_attack_time[final_attacker[0]][final_attacker[1]] = time+1

    # 6. 포탑 정비
    for i in range(N):
        for j in range(M):
            if is_available_potop(i,j):
                if temp_potop[i][j] == potop[i][j]:
                    potop[i][j] += 1
                else :
                    potop[i][j] = temp_potop[i][j]

# 출력
# K번의 턴이 종료된 후 남아있는 포탑 중 가장 강한 포탑의 공격력 출력
result = -1
for i in range(N):
    for j in range(M):
        if result < potop[i][j]:
            result = potop[i][j]

print(result)