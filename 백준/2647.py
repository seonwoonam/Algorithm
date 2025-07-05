# 2647번

# 산성 용액 : 양의 정수
# 알칼리성 용액 : 음의 정수

# 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액 만들기
# 같은산성으로 해도됨.

# N <= 100,000

# 출력
# 특성값이 0에 가장 가까운 두 용액의 특성값 출력. 오름차순으로 / 2개 이상일 경우 아무거나

import sys
MAX = sys.maxsize
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# 투 포인터

# 둘이 만나게 되면 break
# 합의 절댓값이 작으면 왼쪽 이동, 아니면 오른쪽 이동

result = [MAX, MAX]
now_total = MAX

above_zero = N
for i in range(N):
    if arr[i] > 0:
        above_zero = i
        break

behind_zero = -1
for i in range(N):
    if arr[i] < 0:
        behind_zero = i
        break


right = N-1
for left in range(N):
    while right > 0 and left < N and left < right:
        if behind_zero == -1 or arr[left] > 0:
            # 양 양
            if abs(arr[left] + arr[right]) < now_total :
                result[0] = arr[left] 
                result[1] = arr[right] 
                now_total = abs(arr[left] + arr[right])
                right -= 1
            else:
                break
        elif arr[left] < 0 and arr[right] > 0 :
            # 음 양
            if abs(arr[left] + arr[right]) < now_total :
                result[0] = arr[left] 
                result[1] = arr[right] 
                now_total = abs(arr[left] + arr[right])
                
            if abs(arr[left]) > arr[right]:
                break 
            else :
                right -= 1

        elif above_zero == N or arr[right] < 0 :
            # 음 음
            if abs(arr[left] + arr[right]) < now_total :
                result[0] = arr[left] 
                result[1] = arr[right] 
                now_total = abs(arr[left] + arr[right])
                break 
            else:
                right -= 1


result.sort()
print(result[0], result[1])

