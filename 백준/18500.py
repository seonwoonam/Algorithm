#18500
# 동굴에는 미네랄이 저장되어 있으며, 던진 막대기가 미네랄을 파괴할 수도 있다.
# R행 C열
# 비어있거나 미네랄을 포함하고 있으며, 
# 네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 같은 클러스터

# 창영 : 동굴 왼쪽 / 상근 : 동굴 오른쪽
# 막대기 던지는데, 던지기 전에 던질 높이 설정해야 한다.

# 막내가 날아가다가 미네랄을 만나면, 그 칸의 미네랄은 모두 파괴되고 막대는 이동 멈춤

# 미네랄이 파괴된 이후에 남은 클러스터가 분리될 수도 있다.
# 새롭게 생성된 클러스터가 떠있는 경우에는 중력에 의해 바닥으로 떨어짐
# 클러스터는 다른 클러스터나 땅을 만나기 전까지 계속해서 떨어짐.
# 다른 클러스터 위에 떨어지면 그 이후에는 합쳐짐

# 동굴에 있는 미네랄의 모양과 두 사람이 던진 막대의 높이가 주어짐

# 출력
# 모든 막대를 던지고 난 이후에 미네랄 모양을 구하기

# 구현, 탐색
import sys
from collections import deque
R, C = map(int, sys.stdin.readline().rstrip().split())
arr = [
    list(sys.stdin.readline().rstrip())
    for _ in range(R)
]
N = int(sys.stdin.readline().rstrip())
dr = [1,0,-1,0]
dc = [0,-1,0,1]
stick_position_list = list(map(int, sys.stdin.readline().rstrip().split()))
cluster_map = [
    [-1] * C
    for _ in range(R)
]
cluster_index = 0
def in_range(r,c):
    return 0 <= r < R and 0 <= c < C
def BFS(start_r, start_c):
    global cluster_map
    que = deque([])
    que.append((start_r, start_c))
    cluster_map[start_r][start_c] = cluster_index
    while que:
        now_r, now_c = que.popleft()
        for i in range(4):
            next_r = now_r + dr[i]
            next_c = now_c + dc[i]

            if in_range(next_r, next_c) and cluster_map[next_r][next_c] == -1 and arr[next_r][next_c] == 'x': 
                que.append((next_r, next_c))
                cluster_map[next_r][next_c] = cluster_index

    
for turn in range(N):
    now_position = stick_position_list[turn]
    start_r = R-now_position
    start_c = -1
    # 만나면 칸 파괴
    broken_r = -1
    broken_c = -1
    if turn % 2 == 0:
        # 왼쪽에서 시작
        start_c = 0     
        for col in range(0,C):
            if arr[start_r][col] == 'x':
                arr[start_r][col] = '.'
                broken_r = start_r
                broken_c = col
                break
    else :
        start_c = C-1
        for col in range(start_c, -1,-1):
            if arr[start_r][col] == 'x':
                arr[start_r][col] = '.'
                broken_r = start_r
                broken_c = col
                break 

    # 중력
    # 클러스터는 가로로 생성하는게 좋을듯
    # 클러스터의 맨 아래를 찾아야 겠다.
    # start_r 기준으로 처리하면 될듯
    if (broken_r == -1 and broken_c == -1) or broken_r == 0 :
        print("여기")
        continue
    cluster_map = [
        [-1] * C
        for _ in range(R)
    ]
    if arr[broken_r-1][broken_c] == 'x':
        BFS(broken_r-1,broken_c)
    elif in_range(broken_r,broken_c-1) and arr[broken_r][broken_c-1] == 'x':
        BFS(broken_r,broken_c-1)
    elif in_range(broken_r,broken_c+1) and arr[broken_r][broken_c+1] == 'x':
        BFS(broken_r,broken_c+1)
    
    find = False
    for i in range(C):
        if cluster_map[R-1][i] == 0:
            find = True
            break
    if find :
        continue

    while find == False:
        for r in range(R-2,-1,-1):
            for c in range(C):
                if cluster_map[r][c] == 0:
                    if r+2 == R or arr[r+2][c] == 'x':
                        find = True
                    cluster_map[r+1][c] = 0
                    cluster_map[r][c] = -1
                    arr[r+1][c] = 'x'
                    arr[r][c] = '.'

for r in range(R):
    for c in range(C):
        print(arr[r][c], end='')
    print()





