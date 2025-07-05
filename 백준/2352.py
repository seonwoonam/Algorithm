# 연결선이 꼬이지 않으면서 최대 몇 개까지 연결?
# N <= 40,000
import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

lis = []
def binary_search(start, end, value):
    if start == end:
        return start

    mid = (start+end)//2
    if lis[mid] < value:
        return binary_search(mid+1,end,value)
    else :
        return binary_search(start,mid,value)

def binary_search_while(start, end, value):
    while start < end:
        mid = (start+end)//2
        if lis[mid] < value:
            start = mid + 1
        else :
            end = mid

    return start


for i in range(N):
    if len(lis) == 0:
        lis.append(arr[i])
    else :
        if lis[-1] <= arr[i]:
            lis.append(arr[i])
        else :
            idx = binary_search_while(0, len(lis)-1, arr[i])
            lis[idx] = arr[i]

print(len(lis))