# 1697
# 정리 : 
# 해당 문제는 x-1, x+1, 2x 모두 cost가 같기 때문에 BFS로 푸는게 더 좋았을 듯하다
# 하지만 다음과 같이 DP로도 풀 수 있다. 핵심은 35번째 줄의 (i+1)//2 를 사용하여
# DP 방향이 맞으면서도 앞으로 갔다 뒤로 오는거를 반영할 수 있게 풀어야 했다.

# 수빈이 동생과 숨바꼭질
# 수빈이 현재 점 N
# 동생 현재 점 K

# 수빈이 걷거나 순간이동
# x-1 or x+1 / 2x

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
import sys 
MAX = sys.maxsize
N, K = map(int, sys.stdin.readline().rstrip().split())

# k로 가는 최단 시간 구하기
# N, K <= 100,000


DP = [MAX] * 100001
DP[N] = 0
# -1로 움직이기
for i in range(N-1, -1, -1):
    DP[i] = DP[i+1] + 1

# 최종
for i in range(N+1, 100001):
    if i % 2 == 0:
        DP[i] = min(DP[i-1],  DP[i//2]) + 1
    else :
        DP[i] = min(DP[i-1] + 1,DP[(i+1) // 2] + 2)

print(DP[K])