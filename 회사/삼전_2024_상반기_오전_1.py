# 유적지 5 * 5 격자 형태
# 각 칸에는 다양한 유물 조각 배치
# 총 7가지 종류

# 1. 탐사 진행
# 3*3 격자를 선택하여 격자를 회전시킬 수 있다.
# 회전은 시계 방향으로 90, 180, 270도 중 하나의 각도 만큼 가능
# 단, 선택된 격자는 항상 회전을 진행해야만 한다.
# tip : 회전 중심 좌표
# 목표 : 가능한 회전의 방법 중 1차 획득 가치를 최대화하기 v
# 그러한 방법이 여러가지 일 경우 회전한 각도가 가장 작은 방법 선택 v
# 그러한 경우도 여러가지 경우 회전 중심 좌표의 열이 가장 작은 구간
# 그래도 열이 같으면 행이 가장 작은 구간을 선택

# 2. 유물 획득
# 유물 1차 획득
# 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결되어 있음
# -> 3개 이상 연결된 경우 조각이 모여 유물이 되고 사라진다.
# 유물의 가치 == 모인 조각의 개수 v
# 여러개가 한번에 사라질 수 있는거임
# 사라지게 되면 칸이 비게 된다. -> 새로 생겨남

# 유적의 벽면
# 유적의 벽면에는 1~7 사이의 숫자 M개가 적혀있다.
# 유적에서 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보를 담고 있다.
# 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각 생겨난다.
# 새로운 조각은 열번호가 작은 순으로 생성
# 만약 열번호 같다면 행번호가 큰 순서대로 생김

# 단, 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없다.
# 남은 숫자부터 순서대로 사용 가능.

# 더 이상 3개 이상이 연결되지 않아 유물이 될 수 없을 때까지 반복

# 3. 탐사반복
# 위 과정을 총 K턴에 걸쳐 진행
# 각 턴마다 획득한 유물의 가치의 총합을 출력
# 단, 아직 K번 턴을 진행하지 못했지만, 탐사 진행 과정에서 유물을 획득할 수 없었다면 모든 탐사는 종료.
# 종료되는 턴에는 아무 값도 출력하지 않기.

# 단, 초기에 주어지는 유적지는 탐사이전에 유물 발견되지 않으며, 첫번째 턴에서 탐사를 진행한 후
# 항상 유물이 발견됨을 가정해도 좋다.
from collections import deque

ANKLE_90 = 90
ANKLE_180 = 180
ANKLE_270 = 270
K, M = map(int, input().split())
ujekji = []
for _ in range(5):
    first, second, third, fourth, fifth = map(int, input().split())
    ujekji.append([first - 1, second - 1, third - 1, fourth - 1, fifth - 1])
wall_numbers = deque(list(map(int, input().split())))


def in_range(r, c):
    return 0 <= r < 5 and 0 <= c < 5


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [
    [False] * 5
    for _ in range(5)
]


def BFS(start_r, start_c, temp_ujekji, target_umool):
    global visited
    if visited[start_r][start_c]:
        return []
    que = deque([])

    visited[start_r][start_c] = True
    que.append((start_r, start_c))
    path = [(start_r, start_c)]

    while que:
        now_r, now_c = que.popleft()
        for k in range(4):
            next_r = now_r + dr[k]
            next_c = now_c + dc[k]
            if in_range(next_r, next_c) and not visited[next_r][next_c] and temp_ujekji[next_r][next_c] == target_umool:
                visited[next_r][next_c] = True
                que.append((next_r, next_c))
                path.append((next_r, next_c))

    if len(path) >= 3:
        return path
    else:
        return []


def rotate(c_row, c_col, ankle, now_ujekji):
    cycle = 1
    while cycle <= (ankle // 90):
        first = now_ujekji[c_row - 1][c_col - 1]
        second = now_ujekji[c_row - 1][c_col]
        third = now_ujekji[c_row - 1][c_col + 1]

        # 위
        now_ujekji[c_row - 1][c_col - 1] = now_ujekji[c_row + 1][c_col - 1]
        now_ujekji[c_row - 1][c_col] = now_ujekji[c_row][c_col - 1]
        now_ujekji[c_row - 1][c_col + 1] = now_ujekji[c_row - 1][c_col - 1]

        # 왼
        now_ujekji[c_row - 1][c_col - 1] = now_ujekji[c_row + 1][c_col - 1]
        now_ujekji[c_row][c_col - 1] = now_ujekji[c_row + 1][c_col]
        now_ujekji[c_row + 1][c_col - 1] = now_ujekji[c_row + 1][c_col + 1]

        # 아
        now_ujekji[c_row + 1][c_col - 1] = now_ujekji[c_row + 1][c_col + 1]
        now_ujekji[c_row + 1][c_col] = now_ujekji[c_row][c_col + 1]
        now_ujekji[c_row + 1][c_col + 1] = now_ujekji[c_row - 1][c_col + 1]

        # 오
        now_ujekji[c_row - 1][c_col + 1] = first
        now_ujekji[c_row][c_col + 1] = second
        now_ujekji[c_row + 1][c_col + 1] = third

        cycle += 1


for _ in range(K):
    total_value = 0
    umool_value = -1

    umool_info = [
        []
        for _ in range(7)
    ]
    prev_ujekji = [
        [-1] * 5
        for _ in range(5)
    ]

    rotate_ankle = 360
    center_r = 10
    center_c = 10
    umool_value = 0
    # 탐사진행 & 유물획득
    for ANKLE in [ANKLE_270, ANKLE_180, ANKLE_90]:
        for i in range(1, 4):
            for j in range(1, 4):
                visited = [
                    [False] * 5
                    for _ in range(5)
                ]

                temp_umool_info = [
                    []
                    for _ in range(7)
                ]
                temp_umool_value = 0
                temp_rotate_ankle = ANKLE
                temp_center_r = i
                temp_center_c = j
                temp_ujekji = [
                    [-1] * 5
                    for _ in range(5)
                ]
                for temp_row in range(5):
                    for temp_col in range(5):
                        temp_ujekji[temp_row][temp_col] = ujekji[temp_row][temp_col]

                # 돌려서 temp_ujekji 만들고
                rotate(temp_center_r, temp_center_c, temp_rotate_ankle, temp_ujekji)

                # BFS 돌려서 temp_umool_info 만들기
                for row in range(5):
                    for col in range(5):
                        target_umool = temp_ujekji[row][col]
                        temp_list = BFS(row, col, temp_ujekji, target_umool)
                        temp_umool_value += len(temp_list)
                        temp_umool_info[target_umool] += temp_list
                # 이걸 갖고 비교 순위로 비교해서
                if temp_umool_value > umool_value:
                    for umool in range(7):
                        umool_info[umool] = temp_umool_info[umool]
                    umool_value = temp_umool_value
                    rotate_ankle = temp_rotate_ankle
                    center_r =  temp_center_r
                    center_c = temp_center_c
                    for rrr in range(5):
                        for ccc in range(5):
                            prev_ujekji[rrr][ccc] = temp_ujekji[rrr][ccc]

                elif temp_umool_value == umool_value:
                    if temp_rotate_ankle < rotate_ankle:
                        # 넣어주기
                        for umool in range(7):
                            umool_info[umool] = temp_umool_info[umool]
                        umool_value = temp_umool_value
                        rotate_ankle = temp_rotate_ankle
                        center_r = temp_center_r
                        center_c = temp_center_c
                        for rrr in range(5):
                            for ccc in range(5):
                                prev_ujekji[rrr][ccc] = temp_ujekji[rrr][ccc]

                    elif temp_rotate_ankle == rotate_ankle:
                        # 그러한 경우도 여러가지 경우 회전 중심 좌표의 열이 가장 작은 구간
                        if temp_center_c < center_c:
                            for umool in range(7):
                                umool_info[umool] = temp_umool_info[umool]
                            umool_value = temp_umool_value
                            rotate_ankle = temp_rotate_ankle
                            center_r = temp_center_r
                            center_c = temp_center_c
                            for rrr in range(5):
                                for ccc in range(5):
                                    prev_ujekji[rrr][ccc] = temp_ujekji[rrr][ccc]

                        elif temp_center_c == center_c:
                            # 그래도 열이 같으면 행이 가장 작은 구간을 선택
                            if temp_center_r < center_r:
                                for umool in range(7):
                                    umool_info[umool] = temp_umool_info[umool]
                                umool_value = temp_umool_value
                                rotate_ankle = temp_rotate_ankle
                                center_r = temp_center_r
                                center_c = temp_center_c
                                for rrr in range(5):
                                    for ccc in range(5):
                                        prev_ujekji[rrr][ccc] = temp_ujekji[rrr][ccc]


    update_list = []
    # 사라지게 하고, 유적 벽면
    for info_list in umool_info:
        for info in info_list:
            if len(info) > 0:
                update_list.append(info)
                prev_ujekji[info[0]][info[1]] = -1

    update_list.sort(key = lambda x: (x[1], -x[0]))

    for update in update_list:
        now = wall_numbers.popleft()
        prev_ujekji[update[0]][update[1]] = now-1

    for i in range(5):
        for j in range(5):
            ujekji[i][j] = prev_ujekji[i][j]

    total_value += umool_value

    while umool_value != 0 :
        update_list = []
        visited = [
            [False] * 5
            for _ in range(5)
        ]

        umool_value = 0
        for row in range(5):
            for col in range(5):
                target_umool = ujekji[row][col]
                temp_list = BFS(row, col, ujekji, target_umool)
                umool_value += len(temp_list)
                update_list += temp_list

        update_list.sort(key=lambda x: (x[1], -x[0]))
        for update in update_list:
            now = wall_numbers.popleft()
            ujekji[update[0]][update[1]] = now - 1

        total_value += umool_value

    if total_value != 0:
        print(total_value, end=" ")