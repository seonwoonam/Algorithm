# 14658.py
# 떨어지는 별똥별의 수를 최소화해야 한다.
# L*L 트램펄린

# N, M <= 500,000
# L <= 100,000(10**5)
# K <= 100(10**2)

# 출력
# 최대한 많은 별똥별을 튕겨내도록 트램펄린 배치했을 때, 지구에는 몇개의 별똥별이 부딪힐까?
import sys
N, M, L, K = map(int, sys.stdin.readline().rstrip().split())
stars_list = []
for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    stars_list.append((x,y))

# 최대한 많이 어떻게 배치할 것인가?
result_x = []
result_x_count = 0
for now_start in range(N-L+1):
    end = now_start+L
    x_count = 0
    for i in range(K):
        star_x, star_y = stars_list[i]
        if now_start <= star_x <= end:
            x_count += 1

    if x_count > result_x_count:
        result_x_count = x_count
        result_x = [now_start]
    elif x_count == result_x_count:
        result_x.append(now_start)

result_y = []
result_y_count = 0
for now_start in range(M-L+1):
    end = now_start+L
    y_count = 0
    for i in range(K):
        star_x, star_y = stars_list[i]
        if now_start <= star_y <= end:
            y_count += 1

    if y_count > result_y_count:
        result_y_count = y_count
        result_y = [now_start]
    elif y_count == result_y_count:
        result_y.append(now_start)

result = 0
for i in range(len(result_x)):
    now_x = result_x[i]
    now_result = 0
    for j in range(len(result_y)):
        now_y = result_y[j]

        for k in range(K):
            star_x, star_y = stars_list[k]
            if now_x <= star_x <= now_x+L and now_y <= star_y <= now_y+L:
                now_result += 1
    result = max(result, now_result)
    
print(K - result)