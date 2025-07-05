# 횡단보도

# N개의 지역
# 횡단보도 주기 : M분
# 1분마다 신호 바뀜

# 특이사항
# 한주기동안 같은 횡단보도에 파란불이 여러번 들어올 수도 있음

# 출력
# 1번 지역에서 N번지역까지 가는 최소 시간 구하기

# N <= 100,000
# M <= 700,000

# 다익스트라
# 두번돌아야 할수도 있음

import sys 
import heapq
MAX = sys.maxsize
N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [
    []
    for _ in range(N)
]
for i in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    first = first - 1
    second = second - 1

    graph[first].append((i+1,second))
    graph[second].append((i+1,first))

def dijkstra(start):
    dist = [MAX] * N
    que = [] 

    dist[start] = 0

    # 통합 cost, 전 엣지, 노드, turn
    heapq.heappush(que, (0, 0, start, 1))

    while que: 
        cost, edge, node, turn = heapq.heappop(que)
        if dist[node] < cost:
            continue

        for nxt in graph[node]:
            next_edge, next_node = nxt

            next_turn = turn
            total_cost = 0

            if edge < next_edge:
                total_cost = cost + (next_edge - edge)
            else :
                total_cost = turn*M + next_edge
                next_turn = turn+1
            if dist[next_node] > total_cost:
                dist[next_node] = total_cost
                heapq.heappush(que, (total_cost, next_edge, next_node, next_turn))

    return dist[N-1]

print(dijkstra(0))

