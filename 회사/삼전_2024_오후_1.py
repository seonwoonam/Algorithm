# 최단 경로로 공원까지 이동
# M명의 용감한 전사들 메두사 잡기 위해 -> 메두사 향해 최단경로. (어느칸이든 이동가능)
# 전사들이 움직이기 전에 그들을 바라봄으로써 돌로 만들어 멈추기 가능

# 메두사의 이동
# 도로 따라 한 칸이동. 이동한 칸에 전사 있으면 전사 사망
# 여러 최단 경로 가능하다면 상 하 좌 우 우선순위
# 경로 없을 수도 있음

# 메두사의 시선
# 바라보는 방향으로 90도의 시야각 가지며, 시야각 범위 안에 있는 전사들을 볼 수 있다.
# but. 다른 전사에 의해 가려지는 경우 메두사에게 보이지 않음
# 동일한 방향으로 바라본
# 상하좌우 중 가장 많이 볼 수 있는 방향을 봄 -> 우선순위 상화좌우

# 정지
# 정지된 턴에는 움직일 수 없으며 이번 턴이 종료되었을 때 돌에서 풀려남
# 두명이면 모두다 정지

# 전사들의 이동
# 병사들은 메두사를 향해 최대 2칸이동
# 첫번째 이동
# 메두사와 거리를 줄일 수 있는 방향. 상하좌우 우선순위
# 메두사의 시야에 들어오는 곳으로는 이동 불가

# 전사의 공격
# 메두사와 같은 칸에 도달한 전사는 사라짐

# 최단경로는 맨해튼 거리

# 출력
# 메두사가 공원에 도달할 때까지 매턴마다
# 1. 모든 전사가 이동한 거리의 합
# 2. 메두사로 인해 돌이 된 전사의 수
# 3. 메두사를 공격한 전사의 수
# 4. 도착하면 0
# 메두사가 공원까지 가는 도로가 존재하지 않는다면 -1

from collections import deque



N, M = map(int, input().split())
info = list(map(int, input().split()))
s_r = info[0]
s_c = info[1]
e_r = info[2]
e_c = info[3]
soldiers = list(map(int, input().split()))
soldiers_map = [
    [0] * N
    for _ in range(N)
]
for i in range(0, len(soldiers), +2):
    soldiers_map[soldiers[i]][soldiers[i + 1]] += 1
whole_map = [
    list(map(int, input().split()))
    for _ in range(N)
]
# 기타
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


# 메두사 이동 path 찾기
def BFS(start_r, start_c):
    que = deque([])
    visited = [
        [False] * N
        for _ in range(N)
    ]
    que.append(([(start_r, start_c)], start_r, start_c))
    visited[start_r][start_c] = True

    while que:
        path, now_r, now_c = que.popleft()
        if now_r == e_r and now_c == e_c:
            return path

        for k in range(4):
            next_r = now_r + dr[k]
            next_c = now_c + dc[k]

            if in_range(next_r, next_c) and not visited[next_r][next_c] and whole_map[next_r][next_c] != 1:
                que.append((path + [(next_r, next_c)], next_r, next_c))
                visited[next_r][next_c] = True
    return []


path_list = BFS(s_r, s_c)


# 시야각 set 찾는 함수
def find_view(direction, char_r, char_c):
    view = set()
    if direction == 0:
        # 상
        left_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r > -1 and temp_c > -1:
            temp_r -= 1
            temp_c -= 1
            if in_range(temp_r, temp_c):
                left_criterian.append((temp_r, temp_c))

        right_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r > -1 and temp_c < N:
            temp_r -= 1
            temp_c += 1
            if in_range(temp_r, temp_c):
                right_criterian.append((temp_r, temp_c))

        for now in left_criterian:
            r = now[0]
            c = now[1]
            for i in range(r, -1, -1):
                view.add((i, c))
        for i in range(char_r - 1, -1, -1):
            view.add((i, char_c))
        for now in right_criterian:
            r = now[0]
            c = now[1]
            for i in range(r, -1, -1):
                view.add((i, c))

    elif direction == 1:
        # 하
        left_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r < N and temp_c > -1:
            temp_r += 1
            temp_c -= 1
            if in_range(temp_r, temp_c):
                left_criterian.append((temp_r, temp_c))

        right_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r < N and temp_c < N:
            temp_r += 1
            temp_c += 1
            if in_range(temp_r, temp_c):
                right_criterian.append((temp_r, temp_c))

        for now in left_criterian:
            r = now[0]
            c = now[1]
            for i in range(r, N):
                view.add((i, c))
        for i in range(char_r + 1, N):
            view.add((i, char_c))
        for now in right_criterian:
            r = now[0]
            c = now[1]
            for i in range(r, N):
                view.add((i, c))

    elif direction == 2:
        # 좌
        up_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r > -1 and temp_c > -1:
            temp_r -= 1
            temp_c -= 1
            if in_range(temp_r, temp_c):
                up_criterian.append((temp_r, temp_c))

        down_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r < N and temp_c > -1:
            temp_r += 1
            temp_c -= 1
            if in_range(temp_r, temp_c):
                down_criterian.append((temp_r, temp_c))

        for now in up_criterian:
            r = now[0]
            c = now[1]
            for i in range(c, -1, -1):
                view.add((r, i))
        for i in range(char_c - 1, -1, -1):
            view.add((char_r, i))
        for now in down_criterian:
            r = now[0]
            c = now[1]
            for i in range(c, -1, -1):
                view.add((r, i))

    elif direction == 3:
        # 우
        up_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r > -1 and temp_c < N:
            temp_r -= 1
            temp_c += 1
            if in_range(temp_r, temp_c):
                up_criterian.append((temp_r, temp_c))

        down_criterian = []
        temp_r = char_r
        temp_c = char_c
        while temp_r < N and temp_c < N:
            temp_r += 1
            temp_c += 1
            if in_range(temp_r, temp_c):
                down_criterian.append((temp_r, temp_c))

        for now in up_criterian:
            r = now[0]
            c = now[1]
            for i in range(c, N, +1):
                view.add((r, i))
        for i in range(char_c + 1, N, +1):
            view.add((char_r, i))
        for now in down_criterian:
            r = now[0]
            c = now[1]
            for i in range(c, N, +1):
                view.add((r, i))

    return view

# 군인 시야각 set 찾는 함수
def find_soldier_view(direction, soldier_diff, char_r, char_c):
    view = set()
    if direction == 0:
        # 상
        for i in range(char_r - 1, -1, -1):
            view.add((i, char_c))
        if soldier_diff[1] > 0:
            right_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r > -1 and temp_c < N:
                temp_r -= 1
                temp_c += 1
                if in_range(temp_r, temp_c):
                    right_criterian.append((temp_r, temp_c))

            for now in right_criterian:
                r = now[0]
                c = now[1]
                for i in range(r, -1, -1):
                    view.add((i, c))


        elif soldier_diff[1] < 0:
            left_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r > -1 and temp_c > -1:
                temp_r -= 1
                temp_c -= 1
                if in_range(temp_r, temp_c):
                    left_criterian.append((temp_r, temp_c))

            for now in left_criterian:
                r = now[0]
                c = now[1]
                for i in range(r, -1, -1):
                    view.add((i, c))

    elif direction == 1:
        # 하
        for i in range(char_r + 1, N):
            view.add((i, char_c))
        if soldier_diff[1] > 0:
            right_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r < N and temp_c < N:
                temp_r += 1
                temp_c += 1
                if in_range(temp_r, temp_c):
                    right_criterian.append((temp_r, temp_c))

            for now in right_criterian:
                r = now[0]
                c = now[1]
                for i in range(r, N):
                    view.add((i, c))


        elif soldier_diff[1] < 0:
            left_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r < N and temp_c > -1:
                temp_r += 1
                temp_c -= 1
                if in_range(temp_r, temp_c):
                    left_criterian.append((temp_r, temp_c))


            for now in left_criterian:
                r = now[0]
                c = now[1]
                for i in range(r, N):
                    view.add((i, c))



    elif direction == 2:
        # 좌
        for i in range(char_c - 1, -1, -1):
            view.add((char_r, i))

        if soldier_diff[0] > 0:
            down_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r < N and temp_c > -1:
                temp_r += 1
                temp_c -= 1
                if in_range(temp_r, temp_c):
                    down_criterian.append((temp_r, temp_c))

            for now in down_criterian:
                r = now[0]
                c = now[1]
                for i in range(c, -1, -1):
                    view.add((r, i))


        elif soldier_diff[0] < 0:
            up_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r > -1 and temp_c > -1:
                temp_r -= 1
                temp_c -= 1
                if in_range(temp_r, temp_c):
                    up_criterian.append((temp_r, temp_c))

            for now in up_criterian:
                r = now[0]
                c = now[1]
                for i in range(c, -1, -1):
                    view.add((r, i))

    elif direction == 3:
        # 우
        for i in range(char_c + 1, N, +1):
            view.add((char_r, i))

        if soldier_diff[0] > 0:
            down_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r < N and temp_c < N:
                temp_r += 1
                temp_c += 1
                if in_range(temp_r, temp_c):
                    down_criterian.append((temp_r, temp_c))

            for now in down_criterian:
                r = now[0]
                c = now[1]
                for i in range(c, N, +1):
                    view.add((r, i))

        elif soldier_diff[0] < 0:
            up_criterian = []
            temp_r = char_r
            temp_c = char_c
            while temp_r > -1 and temp_c < N:
                temp_r -= 1
                temp_c += 1
                if in_range(temp_r, temp_c):
                    up_criterian.append((temp_r, temp_c))

            for now in up_criterian:
                r = now[0]
                c = now[1]
                for i in range(c, N, +1):
                    view.add((r, i))
    return view

# 거리 구하기
def manhattan(now_x, now_y, target_x, target_y):
    return abs(now_x - target_x) + abs(now_y - target_y)


# 좌우상하
second_move_dr = [0,0,-1,1]
second_move_dc = [-1,1,0,0]

#전체
if len(path_list) == 0:
    print(-1)
else:
    for path in path_list:
        path_r = path[0]
        path_c = path[1]

        if soldiers_map[path_r][path_c] > 0:
            soldiers_map[path_r][path_c] = 0

        if path_r == s_r and path_c == s_c:
            continue
        elif path_r == e_r and path_c == e_c:
            print(0)
        else:
            # 시야각
            frozen_cnt = 0
            selected_view = set()
            for k in range(4):
                view_set = find_view(k, path_r, path_c)
                if k == 0:
                    cnt = 0
                    frozen = set()
                    for i in range(path_r - 1, -1, -1):
                        for j in range(0, N, +1):
                            if soldiers_map[i][j] > 0 and (i, j) in view_set:
                                cnt += soldiers_map[i][j]
                                direct_solder = (i-path_r, j-path_c)
                                solider_view_set = find_soldier_view(k,direct_solder,i, j)
                                for view in solider_view_set:
                                    if view in view_set:
                                        view_set.remove(view)
                    if frozen_cnt < cnt:
                        frozen_cnt = cnt
                        selected_view = view_set
                elif k == 1:
                    cnt = 0
                    frozen = set()
                    for i in range(path_r + 1, N, +1):
                        for j in range(0, N, +1):
                            if soldiers_map[i][j] > 0 and (i, j) in view_set:
                                cnt += soldiers_map[i][j]
                                direct_solder = (i - path_r, j - path_c)
                                solider_view_set = find_soldier_view(k, direct_solder, i, j)
                                for view in solider_view_set:
                                    if view in view_set:
                                        view_set.remove(view)
                    if frozen_cnt < cnt:
                        frozen_cnt = cnt
                        selected_view = view_set
                elif k == 2:
                    cnt = 0
                    frozen = set()
                    for j in range(path_c - 1, -1, -1):
                        for i in range(0, N, +1):
                            if soldiers_map[i][j] > 0 and (i, j) in view_set:
                                cnt += soldiers_map[i][j]
                                direct_solder = (i - path_r, j - path_c)
                                solider_view_set = find_soldier_view(k, direct_solder, i, j)
                                for view in solider_view_set:
                                    if view in view_set:
                                        view_set.remove(view)
                    if frozen_cnt < cnt:
                        frozen_cnt = cnt
                        selected_view = view_set
                elif k == 3:
                    cnt = 0
                    frozen = set()
                    for j in range(path_c + 1, N, +1):
                        for i in range(0, N, +1):
                            if soldiers_map[i][j] > 0 and (i, j) in view_set:
                                cnt += soldiers_map[i][j]
                                direct_solder = (i - path_r, j - path_c)
                                solider_view_set = find_soldier_view(k, direct_solder, i, j)
                                for view in solider_view_set:
                                    if view in view_set:
                                        view_set.remove(view)
                    if frozen_cnt < cnt:
                        frozen_cnt = cnt
                        selected_view = view_set

            # 정지
            # 전사 이동
            distance = 0
            attack_soldier = 0

            temp_soldier_map = [
                [0] * N
                for _ in range(N)
            ]

            for i in range(N):
                for j in range(N):
                    temp_soldier_map[i][j] = soldiers_map[i][j]

            for i in range(N):
                for j in range(N):
                    if soldiers_map[i][j] > 0 and not (i, j) in selected_view:
                        soldier_count = soldiers_map[i][j]
                        # 1. 전사와 메두사 간의 유클리디안 거리 구하기
                        manhattan_distance = manhattan(i,j,path_r,path_c)

                        # 2. 상하좌우로 돌았을 때 유클리디안 거리 1 줄어들고 && 시야 밖이면 그 길 선택. 아니면 for뤂 한번더
                        for k in range(4):
                            next_i = i + dr[k]
                            next_j = j + dc[k]

                            if in_range(next_i, next_j) and not (next_i, next_j) in selected_view:
                                if manhattan_distance > manhattan(next_i, next_j, path_r, path_c):
                                    distance = distance + soldier_count * 1
                                    temp_soldier_map[next_i][next_j] = temp_soldier_map[next_i][next_j] + soldier_count
                                    temp_soldier_map[i][j] = temp_soldier_map[i][j] - soldier_count

                                    # 2-1. 갔을 때 메두사와 같은 칸이면 사라지게
                                    if next_i == path_r and next_j == path_c:
                                        temp_soldier_map[next_i][next_j] = 0
                                        attack_soldier = attack_soldier + soldier_count
                                    break

            for i in range(N):
                for j in range(N):
                    soldiers_map[i][j] = temp_soldier_map[i][j]

            # 3. 좌우상하로 위 과정 한번 더
            for i in range(N):
                for j in range(N):
                    if soldiers_map[i][j] > 0 and not (i, j) in selected_view:
                        soldier_count = soldiers_map[i][j]
                        manhattan_distance = manhattan(i, j, path_r, path_c)

                        for k in range(4):
                            next_i = i + second_move_dr[k]
                            next_j = j + second_move_dc[k]

                            if in_range(next_i, next_j) and not (next_i, next_j) in selected_view:
                                if manhattan_distance > manhattan(next_i, next_j, path_r, path_c):
                                    distance = distance + soldier_count * 1
                                    temp_soldier_map[next_i][next_j] = temp_soldier_map[next_i][next_j] + soldier_count
                                    temp_soldier_map[i][j] = temp_soldier_map[i][j] - soldier_count

                                    if next_i == path_r and next_j == path_c:
                                        temp_soldier_map[next_i][next_j] = 0
                                        attack_soldier = attack_soldier + soldier_count
                                    break

            for i in range(N):
                for j in range(N):
                    soldiers_map[i][j] = temp_soldier_map[i][j]

            # 최종 출력
            print(distance, end=" ")
            print(frozen_cnt, end=" ")
            print(attack_soldier)
