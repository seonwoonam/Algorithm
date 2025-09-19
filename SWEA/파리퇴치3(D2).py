# M의 세기로 분사되면 M칸의 파리를 잡을 수 있음
# + 또는 x 중 하나로 분사
# 한 번에 잡을 수 있는 최대 파리수 출력하기
# 더 최적화 하는 방법 있나?

# dx, dy 테크닉으로 풀 수 있을듯.

T = int(input())

def sibzaga(N, arr, cent_i,cent_j, M):
    center = arr[cent_i][cent_j]
    total = 0
    start = cent_i - M + 1
    if start < 0:
        start = 0
    end = cent_i + M
    if end > N :
        end = N
    for i in range(start, end):
        total += arr[i][cent_j]
    
    start = cent_j - M + 1
    if start < 0:
        start = 0
    end = cent_j + M
    if end > N :
        end = N
    for j in range(start, end):
        total += arr[cent_i][j]
    return total - center

def x(N, arr, cent_i, cent_j, M):
    center = arr[cent_i][cent_j]
    total = 0
    
    i = cent_i - 1
    j = cent_j - 1
    temp_M = M
    while i>=0 and j>= 0 and temp_M > 0:
        total += arr[i][j]
        temp_M -= 1
        i -= 1
        j -= 1

    i = cent_i + 1
    j = cent_j - 1
    temp_M = M
    while i<N and j>= 0 and temp_M > 0:
        total += arr[i][j]
        temp_M -= 1
        i += 1
        j -= 1

    i = cent_i - 1
    j = cent_j + 1
    temp_M = M
    while i>=0 and j<N and temp_M > 0:
        total += arr[i][j]
        temp_M -= 1
        i -= 1
        j += 1

    i = cent_i + 1
    j = cent_j + 1
    temp_M = M
    while i<N and j<N and temp_M > 0:
        total += arr[i][j]
        temp_M -= 1
        i += 1
        j += 1

    return total + center

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    result = 0

    for i in range(N):
        for j in range(N):
            # 십자가
            result = max(result, sibzaga(N,arr,i,j, M))
            # x 모양
            result = max(result, x(N,arr,i,j, M))


    print("#{} {}".format(test_case, result))
