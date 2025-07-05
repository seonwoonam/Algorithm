# 닭싸움 팀 정하기
# 1. 내 친구의 친구는 내 친구이다.
# 2. 내 원수의 원수도 내 친구이다.

# 두 학생이 친구이면 같은 팀
# 같은 팀에 속해 있는 사람들끼리는 전부 친구

# 최대 얼마나 많은 팀이 만들어질 수 있는가?

# E는 원수, F는 친구
# N <= 1000, M <= 5000
# 그리디, 그래프, 구현, DP, 탐색
import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
parents = []
for i in range(N):
    parents.append(i)

def union(a,b):
    global parents
    a = find_parents(a)
    b = find_parents(b)

    if a > b :
        parents[a] = b
    elif a < b :
        parents[b] = a

def find_parents(a):
    global parents
    if parents[a] != a:
        parents[a] = find_parents(parents[a])
    return parents[a]

enemy_relation = [
    set()
    for _ in range(N)
]
for _ in range(M):
    relation, first, second = sys.stdin.readline().rstrip().split()
    first = int(first) - 1
    second = int(second) - 1
    if relation == 'F':
        union(first,second)
    else :
        enemy_relation[first].add(second)
        enemy_relation[second].add(first)

def is_friend(i,j):
    for k in enemy_relation[i]:
        for m in enemy_relation[j]:
            if k == m :
                return True 
    return False

for i in range(N):
    for j in range(i+1, N):
        if is_friend(i,j):
            union(i,j)

result = set()
for i in range(N):
    p = find_parents(i)
    result.add(p)
print(len(result))

N^2 * M