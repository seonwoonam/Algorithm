"""
    2진 트리 모양 초원의 각 노드에 늑대와 향 한마리씩
    루트에서 출발하여 각 노드를 돌면서 양 모으기
    
    내가 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양 잡아먹음
    
    중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양 모아서 돌아오기
    
    0은 양, 1은 늑대
    
    edges : 부모노드, 자식노드
    
    그래프, 탐색, 그리디, DP
    
    info<17
    
    BFS를 통해서 쌓아놓기?
    근데 우선순위 큐 사용?
    
    1. DFS 통해서 양까지 도착하는데 양이 몇마리 필요한지 설정
    2. 우선순위 큐 탑재한 BFS이용해서 풀이
    
    ==> 이렇게 하면 따라 붙는것 까지 계산못함
    
    
    그냥 백트랙킹 문제??
    
"""
import sys
sys.setrecursionlimit(10 ** 8)

result = 0

def dfs(graph, info, now_node, can_reach, now_sheep, now_wolf, visited):
    global result
    next_reach = set()
    
    if now_sheep <= now_wolf:
        return
    result = max(now_sheep, result)
    
    for next_node in can_reach:
        if not visited[next_node]:
            next_reach.add(next_node)
    
    for next_node in graph[now_node]:
        if not visited[next_node]:
            next_reach.add(next_node)
    
    for reach in next_reach:
        if visited[reach] :
            continue
            
        visited[reach] = True
        if info[reach] == 0:  
            dfs(graph, info, reach, next_reach, now_sheep + 1, now_wolf, visited)
        else :
             dfs(graph, info, reach, next_reach, now_sheep, now_wolf+1, visited)
        visited[reach] = False
            
       
def solution(info, edges):
    graph = [
        []
        for _ in range(len(info))
    ]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        
    visited = [False] * len(graph)
    
    visited[0] = True
    dfs(graph, info, 0, set(), 1, 0, visited)
    visited[0] = False
        
    return result