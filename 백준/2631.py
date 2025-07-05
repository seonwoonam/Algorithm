# 2631

# 어렵게 풀었음
# 앞이 이미 정렬된 것이니까 +1 만 해줘도 됨.

# 위치 옮기는 아이들 수를 최소
# N <= 200

# N^4까지도 가능

# 그리디
import sys
N = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

# DP[i] : i까지 확인 했을 때 최대 정렬 길이

DP = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if arr[i] >= arr[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(N - max(DP))