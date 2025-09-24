package 회사;

import java.util.Arrays;
import java.util.Stack;

/*
 * 배열의 회전
 * 
 * ================
 * == 정사각형 회전 ==
 * ================
 * 
 * 90도 시계 방향
 * (i,j) -> (j, n-1-i)
 * 
 * 180도 시계 방향 회전
 * (i,j) -> (n-1-i, n-1-j)
 * 
 * 90도 반시계(270도 시계)
 * (i,j) -> (n-1-j, i)
 * 
 * ================
 * == 직사격형 회전 ==
 * ================
 * 
 * 90도 시계 방향 
 * (i,j) -> (j, R-1-i)
 * 
 * 180도 시계 방향
 * (i,j) -> (R-1-i, C-1-j)
 * 
 * 90도 반시계(270도 시계)
 * (i,j) -> (C-1-j, i)
 * 
 * =============
 * == 부분 회전 ==
 * =============
 * (i,j) -> (j, N-1-i)
 * 
 * 
 * =============
 * == 중력 ==
 * =============
 * 
 * 임시 배열에 담아놓고 밑부터 올라오면서 적용시키기
 */

public class 삼성_배열_연습 {
    public static void main(String[] args) {
        int[][] arr = {{1,2,3,4}, {5,6,7,8},{9,10,11,12}};

        // 직사각형 회전
        int R = arr.length;
        int C = arr[0].length;
        int[][] new_arr = new int[C][R];
        
        for(int i=0; i<R; i++){
            for(int j=0; j<C; j++){
                new_arr[j][R-1-i] = arr[i][j];
            }
        }
        // System.out.println(Arrays.deepToString(new_arr));


        // 부분 회전
        int[][] part_arr = new int[7][7];
        int[][] part_after = new int[7][7];
        int index = 1;
        for(int i=0; i<7;i++){
            for(int j=0; j<7; j++){
                part_arr[i][j] = index++;
            }
        }

        for(int i=0; i<7; i++){
            for(int j=0;j<7;j++){
                part_after[i][j] = part_arr[i][j];
            }
        }

        // 그냥 회전
        // for(int i=2; i<5;i++){
        //     for(int j=2; j<5; j++){
        //         part_after[j][7-1-i] = part_arr[i][j];
        //     }
        // }

        // 상대 좌표 구하기
        for(int i=2; i<5;i++){
            for(int j=2; j<5; j++){
                int r = i-2;
                int c = j-2;
                part_after[2 + c][ 7 - 1 - (2 + r) ] = part_arr[i][j];
            }
        }

        System.out.println(Arrays.deepToString(part_after));


        // 중력
        int[][] gravity_before = {
            {1, 0, 0, 1},
            {0, 1, 0, 0},
            {1, 0, 0, 0}
        };

        int[][] gravity = new int[3][4];

        for(int col = 0; col<4; col++){
            Stack<Integer> st = new Stack();

            for(int row=0; row<3; row++){
                if(gravity_before[row][col] == 1){
                    st.add(1);
                }
            }

            int index_2 = 3-1;
            while(!st.isEmpty()){
                int now = st.pop();
                gravity[index_2--][col] = now;
            }
        }

        System.out.println(Arrays.deepToString(gravity));
    }
    
}
