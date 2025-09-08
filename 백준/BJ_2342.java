import java.io.*;
import java.util.*;

/*
 * 중점 0, 위 1, 왼쪽 2, 아래를 3, 오른쪽을 4라고 정하자
 * 
 * 처음에는 0에서 두 발 시작
 * - 지시 사항에 따라 왼쪽 또는 오른쪽 발을 움직인다. 
 * - 하지만 동시에는 움직이진 않는다. 
 * 
 * 이상한 규칙 
 * - 두 발이 같은 지점에 있는 것을 허락하지 않는다.
 * - 3을 연속으로 눌러야 한다면, 3의 위치에 있는 발로 반복해서 눌러야 한다.
 * 
 * 발이 움직이는 위치에 따라서 드는 힘이 다르다.
 * 중앙에 있던 발이 다른 지점으로 움직일 때, 2의 힘을 사용
 * 
 * 다른 지점에서 인접한 지점 : 3의 힘 사용
 * 
 * 반대편으로 움직일 때는 4의 힘 사용
 * 
 * 같은 지점을 한 번 더 누른다면 1의 힘 사용
 * 
 * 2 + 2 + 1 + 3
 * N <= 100,000
 * 
 * 최소의 힘 출력하기.
 * 
 * 처음에 0에서 시작 
 * (왼쪽 발을 쓰냐, 오른쪽 발을 쓰냐)
 * 
 * DP[i][j][k] : i번까지 왔을 때, 왼쪽 발 위치, 오른쪽 발 위치 최솟값.
 * DP[i][j][k] = min(i-1 에서 오른쪽 발을 옮겨서 현재로 온경우 + value, 왼쪽 발을 옮겨서 현재로 온경우 + value) 
 */

public class BJ_2342 {
        public static void main(String[] args) throws IOException{
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          StringTokenizer st = new StringTokenizer(br.readLine());
          ArrayList<Integer> arr = new ArrayList<>();
          while(st.hasMoreTokens()){
            int n = Integer.parseInt(st.nextToken());
            if(n == 0) break;
            arr.add(n);
          }

          int[][][] DP = new int[arr.size()][5][5];
          for(int i=0; i<arr.size(); i++){
            for(int j=0; j<5; j++){
                for(int k=0; k<5;k++){
                    DP[i][j][k] = 1000000;
                }
            }
          }

          DP[0][arr.get(0)][0] = 2;
          DP[0][0][arr.get(0)] = 2;

          for(int i=1; i<arr.size(); i++){
            int now_pos = arr.get(i);
            int before_pos = arr.get(i-1);

            // 왼발에 before_pos 
            int value = 0;
            if(before_pos == 0){
                value = 2;
            }else if(Math.abs(now_pos - before_pos) == 2){
                value = 4;
            }else if(Math.abs(now_pos - before_pos) == 1 || Math.abs(now_pos - before_pos) == 3){
                value = 3;
            }else if(now_pos == before_pos){
                value = 1;
            }
            // 왼발을 옮기는 경우
            for(int j=0; j<5; j++){
                if(now_pos == j) continue;
                DP[i][now_pos][j] = Math.min(DP[i][now_pos][j], DP[i-1][before_pos][j] + value);
            }

            // before pos가 아닌 발 옮기기
            if(now_pos != before_pos){
                for(int j=0; j<5; j++){
                    if(j == 0){
                        value = 2;
                    }else if(Math.abs(now_pos - j) == 2){
                        value = 4;
                    }else if(Math.abs(now_pos - j) == 1 || Math.abs(now_pos - j) == 3){
                        value = 3;
                    }else if(now_pos == j){
                        value = 1;
                    }
                    DP[i][before_pos][now_pos] = Math.min(DP[i][before_pos][now_pos], DP[i-1][before_pos][j] + value);
                    DP[i][now_pos][before_pos] = Math.min(DP[i][now_pos][before_pos], DP[i-1][j][before_pos] + value);
                }
            }
            
            // 오른발, Before_pos 오른발을 옮기는 경우
            if(before_pos == 0){
                value = 2;
            }else if(Math.abs(now_pos - before_pos) == 2){
                value = 4;
            }else if(Math.abs(now_pos - before_pos) == 1 || Math.abs(now_pos - before_pos) == 3){
                value = 3;
            }else if(now_pos == before_pos){
                value = 1;
            }
            // 왼발을 옮기는 경우
            for(int j=0; j<5; j++){
                if(now_pos == j) continue;
                DP[i][j][now_pos] = Math.min(DP[i][j][now_pos], DP[i-1][j][before_pos] + value);
            }
          }

            int result = Integer.MAX_VALUE;


       
            for(int i=0; i<5; i++){
                result = Math.min(DP[arr.size()-1][arr.get(arr.size()-1)][i], result);
                result = Math.min(DP[arr.size()-1][i][arr.get(arr.size()-1)], result);
            }
            
            // System.out.println(Arrays.deepToString(DP));
            System.out.println(result);

        }
}
