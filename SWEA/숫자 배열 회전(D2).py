T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

# 90도 회전
# 회전 후의 행번호 = 회전 전의 열번호
# 회전 후의 열번호 = N - 1 - 회전 전의 행번호

# 180도 회전
# 회전 후의 행번호 = N - 1 - 회전 전의 행번호
# 회전 후의 열번호 = N - 1 - 회전 전의 열번호

# 270도 회전
# 회전 후의 행번호 = N - 1 - 회전 전의 열번호
# 회전 후의 열번호 = 회전 전의 행번호

# N * N 행렬이 주어질 때,
# 90도, 180도, 270도 회전한 모양 출력
for test_case in range(1, T + 1):
    N = int(input())
    arr = [
        list(map(int,input().split()))
        for _ in range(N)
    ]

    arr_90 = [
        [0] * N
        for _ in range(N)
    ]

    arr_180 = [
        [0] * N
        for _ in range(N)
    ]

    arr_270 = [
        [0] * N
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            arr_90[j][N-1-i] = arr[i][j]
            arr_180[N-1-i][N-1-j] = arr[i][j]
            arr_270[N-1-j][i] = arr[i][j]

    print("#{}".format(test_case))
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(arr_180[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(arr_270[i][j], end="")
        print()