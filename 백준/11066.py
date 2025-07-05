# 5:13

# 두 개의 파일을 합칠 때 필요한 비용 : 두 파일의 크기의 합

# 결과
# 한 개의 파일을 완성하는데 필요한 최소비용

# 비용을 최대한 적게 만들어서 더하는게 좋음

# 그리디 -> DP
# K <= 500

# 순서가 바뀌면 안됨 
# DP

# 합치게 된 후로 계산을 한다는거는 계속 영향을 준다는 것이기 때문에 어떻게 풀어야할지 모르겠음

import sys 
MAX = sys.maxsize

T = int(input())
arr = [
    []
    for _ in range(T)
]

for i in range(T):
    size = int(input())
    arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))

for now_arr in arr:
    size = len(now_arr)
    # DP[i][j] = i에서 j까지 합하는데 필요한 최소비용
    # DP[i][j] = 
    # sum(i,j) + min(DP[i][x] + DP[x+1][j])
    # 어떤 식으로 순회할지도 생각

    DP = [
        [MAX] * size
        for _ in range(size)
    ]

    for i in range(size):
        DP[i][i] = 0

    sum_arr = [
        [MAX] * size
        for _ in range(size)
    ]  

    for i in range(size):
        for j in range(size):
            sum_arr[i][j] = sum(now_arr[i:j+1])


    for i in range(size-1, -1, -1):
        for j in range(i,size):
            for k in range(0, j-i):
                DP[i][j] = min(DP[i][j], sum_arr[i][j] + DP[i][i+k] + DP[i+k+1][j])
                
    print(DP[0][size-1])
