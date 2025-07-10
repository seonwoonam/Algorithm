T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 서로 마주보는 숫자들은 곱한 뒤 모두 더할 때 최댓값?
# 개선한다하면 sliding window 로 구현하는 방식으로 시간 복잡도 개선 가능할듯

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0

    if N == M:
        for i in range(N):
            result += A[i] * B[i]
    elif N > M :
        # B를 움직여야함
        for i in range(N):
            temp = 0
            if i + M > N:
                break
            for j in range(M):
                temp += A[i+j] * B[j]
            result = max(result, temp)

    elif N < M :
        for i in range(M):
            temp = 0
            if i + N > M:
                break
            for j in range(N):
                temp += A[j] * B[i+j]
            result = max(result, temp)

    print("#{} {}".format(test_case, result))