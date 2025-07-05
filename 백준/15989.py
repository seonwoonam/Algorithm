# 정수 N이 주어졌을 때 1,2,3의 합으로 나타내는 방법의 수 구하기
# N <= 10,000

# DP
T = int(input())
arr = [
    int(input())
    for _ in range(T)
]

DP = [1] * 10001
for i in range(2,10001):
    DP[i] = DP[i] + DP[i-2]

for i in range(3, 10001):
    DP[i] = DP[i] + DP[i-3]

for number in arr:
    print(DP[number])

# 위 방법외에도 아래와 같은 방법도 가능

# DP[i][1]: 정수 i를 만들 때 1로 끝나는 경우 -> 그 이전에 1만 올 수 있다.
# DP[i][2]: 정수 i를 만들 때 2로 끝나는 경우 -> 그 이전에 1과 2가 올 수 있다.
# DP[i][3]: 정수 i를 만들 때 3으로 끝나는 경우 -> 그 이전에 1과 2와 3이 올 수 있다.

# DP[i][1] = DP[i-1][1]
# DP[i][2] = DP[i-2][1] + DP[i-2][2]
# DP[i][3] = DP[i-3][1] + DP[i-3][2] + DP[i-3][3]