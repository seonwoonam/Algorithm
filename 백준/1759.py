# 증가하는 순서로 배열
# 사용했을 법한 문자의 종류 C가지

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

def comb(comb_arr, index):
    if len(comb_arr) == L:
        find = 0
        find_ja = 0
        for str in comb_arr:
            if str in {'a','e','i','o','u'}:
                find += 1
            else :
                find_ja += 1
        if find >=1 and find_ja >= 2 :
            for str in comb_arr:
                print(str, end='')
            print()
        return
    else :
        for i in range(index, len(arr)):
            comb_arr.append(arr[i])
            comb(comb_arr, i+1)
            comb_arr.pop()

comb([], 0)
