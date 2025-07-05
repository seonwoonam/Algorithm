# 쓰레기로 차있는 칸을 되도록 적게 지나가기
# 되도록 적게 지나가는 경우의 수가 여러개이면, 쓰레기 옆을 지나가는 개수를 최소화
# S와 F는 세지않기

# 3 <= N, M <= 50

# 출력
# 지나가는 쓰레기의 최소 개수, 쓰레기 옆을 지나가는 칸의 개수
import sys
import heapq

NEAR = 10000
GARBAGE = 100000000
MAX = sys.maxsize

N,M = map(int, sys.stdin.readline().rstrip().split())
arr = [
    list(sys.stdin.readline().rstrip())
    for _ in range(N)
]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def in_range(x,y):
    return 0<=x<N and 0<=y<M

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S' :
            start_x = i
            start_y = j
        elif arr[i][j] == '.':
            for k in range(4):
                next_i = i+dx[k]
                next_j = j+dy[k]

                if in_range(next_i,next_j) and arr[next_i][next_j] == 'g':
                    arr[i][j] = 'n'

def dijkstra(start_x, start_y):
    que = []
    dist = [
        [MAX] * M
        for _ in range(N)
    ]
    # cost, x, y, garbage, near
    heapq.heappush(que, (0, start_x, start_y, 0, 0))
    dist[start_x][start_y] = 0

    while que:
        cost, x, y, garbage, near = heapq.heappop(que)
        
        if dist[x][y] < cost :
            continue

        for i in range(4):
            next_x = dx[i] + x
            next_y = dy[i] + y

            if in_range(next_x, next_y) :
                if arr[next_x][next_y] == 'n':
                    next_cost = cost + NEAR
                    if dist[next_x][next_y] > next_cost:
                        dist[next_x][next_y] = next_cost
                        heapq.heappush(que, (next_cost, next_x, next_y, garbage, near+1))
                elif arr[next_x][next_y] == 'g':
                    next_cost = cost + GARBAGE
                    if dist[next_x][next_y] > next_cost:
                        dist[next_x][next_y] = next_cost
                        heapq.heappush(que, (next_cost, next_x, next_y, garbage+1, near))
                elif arr[next_x][next_y] == 'F':
                    return garbage, near
                else :
                    next_cost = cost + 1
                    if dist[next_x][next_y] > next_cost:
                        dist[next_x][next_y] = next_cost
                        heapq.heappush(que, (next_cost, next_x, next_y, garbage, near))

            
result1, result2 = dijkstra(start_x, start_y)
print("{} {}".format(result1, result2))