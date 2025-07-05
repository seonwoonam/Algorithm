# 로봇 조종하기 2169
# 11:44

# 위쪽으로 이동못하고, 한 번 탐사한 지역 탐사 x
# 1,1 -> N,M
# 탐사한 지역들의 가치의 합이 최대로

# N, M <= 1000

import sys 
MIN = -sys.maxsize
N,M = map(int, sys.stdin.readline().rstrip().split())
arr = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(N)
]

# DP

# DP[i][j] = i,j까지 왔을 때 최대 가치
# DP[i][j] = max()
# DP[i-1][j], DP[i][j-1], DP[i][j+1]

DP = [
    [MIN] * (M) 
    for _ in range(N)
]

DP_LEFT = [
    [MIN] * (M) 
    for _ in range(N)
]

DP_RIGHT = [
    [MIN] * (M) 
    for _ in range(N)
]

DP[0][0] = arr[0][0]
DP_LEFT[0][0] = arr[0][0]
DP_RIGHT[0][0] = arr[0][0]

for i in range(1,M):
    DP[0][i] = DP[0][i-1] + arr[0][i]
    DP_LEFT[0][i] = DP_LEFT[0][i-1] + arr[0][i]
    DP_RIGHT[0][i] = DP_RIGHT[0][i-1] + arr[0][i]

for i in range(1,N):
    # 왼쪽 먼저 업데이트
    DP_LEFT[i][0] = DP[i-1][0] + arr[i][0]
    for j in range(1, M):
        DP_LEFT[i][j] = max(DP[i-1][j], DP_LEFT[i][j-1])  + arr[i][j]

    # 오른쪽 업데이트
    DP_RIGHT[i][M-1] = DP[i-1][M-1] + arr[i][M-1]
    for j in range(M-2, -1, -1):
        DP_RIGHT[i][j] = max(DP[i-1][j], DP_RIGHT[i][j+1])  + arr[i][j]

    # 최종 업데이트
    for j in range(0,M):
        DP[i][j] = max(DP_LEFT[i][j], DP_RIGHT[i][j], DP[i-1][j] + arr[i][j])

print(DP[N-1][M-1])