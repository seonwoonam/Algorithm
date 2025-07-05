# 특정 건물을 가장 빨리 짓기까지 걸리는 최소시간
# 위상정렬

import sys 
from collections import deque
T = int(sys.stdin.readline().rstrip())
N_arr = []
K_arr = []
build_time = [
    []
    for _ in range(T)
]
graph_all = []
indegree_graph_all = []
indegree_all = []
goal_all = []

for i in range(T):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    N_arr.append(N)
    K_arr.append(K)

    build_time[i] = list(map(int, sys.stdin.readline().rstrip().split()))

    graph = [
        []
        for _ in range(N)
    ]

    indegree_graph = [
        []
        for _ in range(N)
    ]

    indegree = [0] * N
    for _ in range(K):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        graph[start-1].append(end-1)
        indegree_graph[end-1].append(start-1)
        indegree[end-1] += 1

    goal = int(sys.stdin.readline().rstrip()) - 1


    graph_all.append(graph)
    indegree_graph_all.append(indegree_graph)
    indegree_all.append(indegree)
    goal_all.append(goal)



for i in range(T):
    graph = graph_all[i]
    indegree_graph = indegree_graph_all[i]
    indegree = indegree_all[i]
    goal = goal_all[i]
    time = build_time[i]

    path = set()

    # 자기한테 오는 건물을 알아야함
    # BFS => DP 때문에 필요없어짐.
    que = deque()
    que.append(goal)
    path.add(goal)

    visited = [False] * N_arr[i]
    visited[goal] = True

    while que:
        now_node = que.popleft()

        for next_node in indegree_graph[now_node]:
            if visited[next_node] != True:
                visited[next_node] = True
                que.append(next_node)
                path.add(next_node)
        
    que = deque()
    
    # 위상정렬 + DP
    DP = [-1] * N_arr[i]

    for j in range(len(indegree)):
        if indegree[j] == 0:
            DP[j] = time[j]
            que.append(j)

    while que:
        now_node = que.popleft()
        if not now_node in path:
            continue
        
        for prev_node in indegree_graph[now_node]:
            DP[now_node] = max(DP[now_node], DP[prev_node] + time[now_node])


        if now_node == goal:
            break
        
        for next_node in graph[now_node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                que.append(next_node)


    print(DP[goal])