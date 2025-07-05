# N개의 영단어들이 주어졌을 때 가장 비슷한 두 단어 구하기
# 접두사 겹치는 것
# 접두사의 길이가 최대인 경우가 여러 개일 때는 입력되는 순서 제일 앞쪽에 있는 답

# N <= 20000

# 최대 n^2
# 길이 100자 이하

# nlogn 같은걸로 했다가 100자 비교해야 할듯
# 그리디

# 풀이
# 정렬 -> 위아래 비교 -> 접두사 찾기 -> 마지막 순서대로 돌아가면서 찾기

import sys 
N = int(input())
MAX_SIZE = sys.maxsize
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

max = 0
S = ''
T = ''

selected_group = set()
sorted_arr = sorted(arr)
count = 0

for i in range(1,N-1):
    # 앞에꺼 확인
    count = 0

    for k in range(0,len(sorted_arr[i])):
        if k<len(sorted_arr[i-1]) and sorted_arr[i][k] == sorted_arr[i-1][k]:
            count += 1
        else :
            break

    if count > max:
        max = count
        selected_group= {sorted_arr[i][0:count]}
    elif count == max and count != 0:
        selected_group.add(sorted_arr[i][0:count])

    # 뒤에꺼 확인
    count = 0

    for k in range(0,len(sorted_arr[i])):
        if k<len(sorted_arr[i+1]) and sorted_arr[i][k] == sorted_arr[i+1][k]:
            count += 1
        else :
            break

    if count > max:
        max = count
        selected_group= {sorted_arr[i][0:count]}
    elif count == max and count != 0:
        selected_group.add(sorted_arr[i][0:count])

index = MAX_SIZE 
S = '' 
T = ''
headStr = ''

for string in selected_group:
    length = len(string)
    for i in range(N):
        if arr[i][0:length] == string:
            if index > i:
                index = i
                headStr = string
                S = arr[i]
            break

for i in range(N):
    length = len(headStr)
    if arr[i][0:length] == headStr and arr[i] != S:
        T = arr[i]
        break

print(S)
print(T)