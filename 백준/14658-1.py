# 하늘에서 별똥별이 빗발친다 14658번
# 최대한 많은 별똥별을 우주로 튕겨내기
# L*L 크기

# 출력
# 지구에는 몇 개의 별똥별이 부딪히게 될까? (최소)

# N, M <= 500,000
# L <= 100,000
# K <= 100

import sys 
N,M,L,K = map(int, sys.stdin.readline().rstrip().split())
stars = [] 
for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    stars.append((x,y))

# 지구에 부딪히는 거 = 내려오는거 - 튕겨내는거
# 그냥 탐색은 안됨
# K를 활용해야함
# 각각의 별들을 모서리로 보낼 때 가장 많이 커버하는 것 찾기

result = 0

for star in stars:
    x, y = star 
    x_y_list = set()
    
    #상
    for i in range(L,-1,-1):
        now_x_start = x - i
        now_y_start = y-L
        now_x_end = x+(L-i)
        now_y_end = y

        x_y_list.add((now_x_start, now_y_start, now_x_end, now_y_end))

    #우
    for i in range(L,-1,-1):
        now_x_start = x - L
        now_y_start = y-i
        now_x_end = x
        now_y_end = y+(L-i)

        x_y_list.add((now_x_start, now_y_start, now_x_end, now_y_end))


    #하
    for i in range(L,-1,-1):
        now_x_start = x - i
        now_y_start = y
        now_x_end = x+(L-i)
        now_y_end = y + L

        x_y_list.add((now_x_start, now_y_start, now_x_end, now_y_end))


    #좌
    for i in range(L,-1,-1):

        now_x_start = x
        now_y_start = y-i
        now_x_end = x + L
        now_y_end = y+(L-i)

        x_y_list.add((now_x_start, now_y_start, now_x_end, now_y_end))

        
    for x_y in x_y_list :
        count = 0
        now_x_start = x_y[0]
        now_y_start = x_y[1]
        now_x_end = x_y[2]
        now_y_end = x_y[3]

        for star2 in stars:
            x2, y2 = star2

            if now_x_start<=x2<=now_x_end and now_y_start<=y2<=now_y_end :
                count += 1
        result = max(result,count)


print(K-result)