# N개의 수 중에서 어떤 수가 다른 수 두개의 합 => Good
# 좋은 수 몇개인지 출력

# N <= 2000
# 투 포인터 반대로 오는 것도 생각하면 좋을 듯. 투포인터 while문으로 구현하는게 더 편하려나
import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

good_count = 0 

for i in range(N):
    now = arr[i]
    start = 0
    end = N-1

    while start < end:
        if start == i :
            start += 1
            continue
        if end == i :
            end -= 1
            continue

        if arr[start] + arr[end] == now:
            good_count += 1
            break
        elif arr[start] + arr[end] > now:
            end -= 1
        else :
            start += 1


print(good_count)
