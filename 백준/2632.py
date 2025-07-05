# 2632번
# 2종류의 피자 A와 B 판매

# 각 조각에 쓰여진 숫자는 피자조각의 크기를 나타냄

# 조건
# 한 종류의 피자를 2조각 이상 판매할 때는 반드시 연속된 조각을 잘라서 판매해야함
# 이때 판매한 피자조각의 크기의 합이 주문한 크기가 되어야함

# 혼합시켜도됨.

# 피자가게에서 손님이 원하는 크기의 피자를 판매하는 모든 방법의 가지 수 계산

# 피자의 크기 <= 2,000,000
# M,N <= 1000
# 각 피자조각의 크기 <= 1000

# 출력
# 피자를 판매하는 방법의 가지수
# 없을 경우에는 숫자 0 출력
import sys
SIZE = int(sys.stdin.readline().rstrip())
M, N = map(int, sys.stdin.readline().rstrip().split())
A_SIZE_LIST = []
B_SIZE_LIST = []
for _ in range(M):
    A_SIZE_LIST.append(int(sys.stdin.readline().rstrip()))
for _ in range(N):
    B_SIZE_LIST.append(int(sys.stdin.readline().rstrip()))

# 옆에 있는거 확인할때는 나머지 값 사용해서 회전할 수 있도록.
# 투 포인터? 1000 * 1000안에 끝내기 가능할듯.

# 1. 자기안에서 투 포인터로 끝내기
    # 끝내면서 합 리스트을 만들어놓기
    # left가 다시 원점으로 돌아오면 게임끝나느거임
A_SUM_LIST = [0]
B_SUM_LIST = [0]

result = 0
for window_size in range(1,M):
    s_sum = 0
    for i in range(window_size):
        s_sum += A_SIZE_LIST[i]
    if s_sum <= SIZE:    
        A_SUM_LIST.append(s_sum)
    for i in range(1,M):
        right = (i+window_size-1)%M
        s_sum -= A_SIZE_LIST[i-1]
        s_sum += A_SIZE_LIST[right]
        if s_sum <= SIZE:
            A_SUM_LIST.append(s_sum)
total_sum = sum(A_SIZE_LIST)
if SIZE >= total_sum:
    A_SUM_LIST.append(total_sum)


for window_size in range(1,N):
    s_sum = 0
    for i in range(window_size):
        s_sum += B_SIZE_LIST[i]
    if s_sum <= SIZE:
        B_SUM_LIST.append(s_sum)
    for i in range(1,N):
        right = (i+window_size-1)%N
        s_sum -= B_SIZE_LIST[i-1]
        s_sum += B_SIZE_LIST[right]
        if s_sum <= SIZE:
            B_SUM_LIST.append(s_sum)

total_sum = sum(B_SIZE_LIST)
if SIZE >= total_sum:
    B_SUM_LIST.append(total_sum)

A_SUM_LIST.sort()
B_SUM_LIST.sort(reverse=True)

A_dict = dict()
for a_sum in A_SUM_LIST:
    if a_sum in A_dict.keys():
        A_dict[a_sum] += 1
    else :
        A_dict[a_sum] = 1

B_dict = dict()
for b_sum in B_SUM_LIST:
    if b_sum in B_dict.keys():
        B_dict[b_sum] += 1
    else :
        B_dict[b_sum] = 1

NEW_A_SUM_LIST = [A_SUM_LIST[0]]
for a_sum in A_SUM_LIST:
    if NEW_A_SUM_LIST[-1] != a_sum:
        NEW_A_SUM_LIST.append(a_sum)
NEW_B_SUM_LIST = [B_SUM_LIST[0]]
for b_sum in B_SUM_LIST:
    if NEW_B_SUM_LIST[-1] != b_sum:
        NEW_B_SUM_LIST.append(b_sum)

right = 0
for now_a in NEW_A_SUM_LIST:
    target = SIZE - now_a

    while right < len(NEW_B_SUM_LIST) and target <= NEW_B_SUM_LIST[right]:
        if target < NEW_B_SUM_LIST[right]:
            right+=1
        elif target == NEW_B_SUM_LIST[right]:
            result = result + (A_dict[now_a] * B_dict[target])
            right += 1
         
print(result)