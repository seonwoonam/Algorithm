#1800
# 학생들의 번호가 1부터 N까지 붙여져 있고, 아무나 서로 연결되어 있지 않다.
# P개의 쌍만이 서로 이어질 수 있으며 서로 연결하는데 가격이 다르다.
# 1번은 인터넷됨
# 목표는 N번 컴퓨터가 인터넷 연결(나머지는 상관없음)
# K개의 인터넷 선은 공짜로 연결
# 나머지 인터넷 선에 대해서는 남은 것 중 제일 비싼 것에 대해서만 가격받음

# 출력
# 내게되는 최소 가격 구하기
# 안되면 -1 출력

# 조건
# N, K <= 1000
# P <= 10,000

# 풀이방법
# 이분탐색 + 다익스트라
# 기준가격 이하는 어차피 카운트 하지 않기 때문에 무료로 지나가는 가격, 기준가격 초과는 K횟수를 사용해야하는 가격임으로 다익스트라 돌면서 누적시킴
# 위 과정을 돌면서 기준 가격을 찾아내는 방법으로 최소 가격을 찾을 수 있음
import sys 
import heapq
MAX = sys.maxsize
N,P,K = map(int, sys.stdin.readline().rstrip().split())
graph = [
    []
    for _ in range(N)
]
for i in range(P):
    node1, node2, cost = map(int, sys.stdin.readline().rstrip().split())
    node1 = node1 - 1
    node2 = node2 - 1
    graph[node1].append((cost,node2))
    graph[node2].append((cost,node1))


def dijkstra(start_node, limit):
    dist = [MAX] * N 
    que = []
    heapq.heappush(que, (0,start_node))
    dist[start_node] = 0
    while que :
        cost, now_node = heapq.heappop(que)
    
        if cost > dist[now_node]:
            continue

        for next_node_info in graph[now_node]:
            next_cost = next_node_info[0]
            next_node = next_node_info[1]

            if next_cost > limit :
                if dist[next_node] > (cost + 1):
                    heapq.heappush(que,(cost+1, next_node))
                    dist[next_node] = cost + 1
            else :
                if dist[next_node] > cost:
                    heapq.heappush(que,(cost, next_node))
                    dist[next_node] = cost
        
    if dist[N-1] > K :
        return False 
    else :
        return True

answer = -1
left = 0 
right = 1000000

while left <= right:
    mid = (left + right) // 2
    flag = dijkstra(0,mid)
    if flag :
        answer = mid 
        right = mid-1
    else :
        left = mid + 1

print(answer)