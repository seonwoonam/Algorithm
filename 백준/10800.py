#10800
# 교훈 : DP같이 않게 풀이하는 경우(ex min,max사용안함) 앞부분을 바로 참조하는거는 중복된게 너무 많을 때 위험이 있을 수 있다! 총 합에서 빼나가는게 좋은듯.

# 여러 플레이어 참여
# 각 플레이어는 특정한 색과 크기를 가진 자기 공 하나를 조종하여 게임

# 목표 : 자기 공보타 크기가 작고 색이 다른 공을 사로잡아 그 공의 크기만큼의 점수를 얻는 것
# 다른 공을 사로잡은 이후에도 본인의 색과 크기는 변하지 않는다.


# 각 플레이어가 사로잡을 수 있는 모든 공들의 크기의 합 출력하기
# N <= 200,000
# 색상 <= 200,000
# 크기 <= 2,000
import sys 
N = int(sys.stdin.readline().rstrip())
ball_list = []
# 같은 색상 현재까지 나온 sum
score_sum = dict()
# 같은 점수 현재까지 나온 점수합
weight_count = dict()
for i in range(N):
    c, s = map(int, sys.stdin.readline().rstrip().split())
    ball_list.append((c,s,i))

for i in range(N):
    now_color, now_score,now_index = ball_list[i]
    score_sum[now_color] = 0

for i in range(N):
    now_color, now_score,now_index = ball_list[i]
    weight_count[now_score] = 0

ball_list.sort(key=lambda x : (x[1], x[0]))

result = [0] * N
score_sum[ball_list[0][0]] = ball_list[0][1]
weight_count[ball_list[0][1]] = ball_list[0][1]
sum_total = ball_list[0][1]
for i in range(1,N):
    now_color, now_score,now_index = ball_list[i]
    before_color, before_score,before_index = ball_list[i-1]

    if before_color == now_color and before_score == now_score:
        result[now_index] = result[before_index]
    else :
        result[now_index] = sum_total - score_sum[now_color] - weight_count[now_score]

    weight_count[now_score] += now_score
    score_sum[now_color] += now_score
    sum_total += now_score

for score in result :
    print(score)
