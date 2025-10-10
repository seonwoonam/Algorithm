"""
    N * M 크기의 행렬
    
    내구도가 0이하가 되면 파괴된다.
    반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 한다.
    
    N <= 1,000
    M <= 1,000
    
    skill <= 2.5 * 10^5
    
    skill을 바로 적용하면 안된다.-> 시간복잡도 터짐
    누적합 처럼 구현

    누적합을 구현하는 아이디어를 떠올리는게 어려운 문제
"""

def solution(board, skill):
    answer = 0
    row_len = len(board)
    col_len = len(board[0])
    
    acc_arr = [
        [0] * (col_len+1)
        for _ in range(row_len+1)
    ]
    
    for sk in skill :
        type = sk[0]
        r1 = sk[1]
        c1 = sk[2]
        r2 = sk[3]
        c2 = sk[4]
        degree = sk[5]
            
        if type == 1:
            # 공격
            mul = -1    
        else :
            # 회복
            mul = 1
        
        acc_arr[r1][c1] += (mul * degree)
        acc_arr[r1][c2+1] -= (mul * degree)
        acc_arr[r2+1][c1] -= (mul * degree)
        acc_arr[r2+1][c2+1] += (mul * degree)
        
    for i in range(row_len + 1):
        for j in range(col_len):
            acc_arr[i][j+1] += acc_arr[i][j]

    for j in range(col_len + 1):
        for i in range(row_len):
            acc_arr[i+1][j] += acc_arr[i][j]
        
    for i in range(row_len):
        for j in range(col_len):
            if acc_arr[i][j] + board[i][j] >= 1:
                answer += 1
        
    return answer