# N개의 컴퓨터 모두 연결되게 하고 싶음
# 최소로 연결하기
# MST

import sys 
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline().rstrip())
edges = []
for i in range(N):
    input = list(sys.stdin.readline().rstrip())
    for j in range(len(input)):
        if input[j] == '0':
            continue 
        else :
            if 'a' <= input[j] <= 'z':
                edges.append((ord(input[j]) - ord('a') + 1,i,j))
            elif 'A' <= input[j] <= 'Z':
                edges.append((ord(input[j]) - ord('A') + 27,i,j))

parents = [-1] * N 
total = 0
for i in range(len(edges)):
    total = total + edges[i][0]


for i in range(N):
    parents[i] = i

def union(a,b):
    global parents
    a = parents[a]
    b = parents[b]

    if a <= b:
        parents[b] = a
    else:
        parents[a] = b

def find_parents(a):
    global parents
    if parents[a] != a:
        parents[a] = find_parents(parents[a])
    return parents[a]
    

edges.sort()
for edge in edges:
    length, start, end = edge 
    if start == end:
        continue
    
    if find_parents(start) != find_parents(end):
        union(start, end)
        total = total - length


result = total
parents[0] = find_parents(parents[0])
for i in range(1,N):
    if find_parents(parents[i]) != parents[0]:
        result = -1
        
print(result)
