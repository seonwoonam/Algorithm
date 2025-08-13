import java.io.*;


/*
  N Queen 
  전체조건을 쪼개보자.
  하나의 행에 하나의 퀸 배치를 전제조건
   
  각각 열과, 대각선들을 기록해둠. 
  1. boolean 배열 풀이법
  2. 비트마스킹 풀이범
 */
public class BJ_9663 {

    static int N; 
    static int result = 0;
    static int[] dx = {1,1,-1,-1};
    static int[] dy = {-1,1,1,-1};

    public static boolean in_range(int x, int y){
        return 0<=x && x<N && 0<=y && y<N;
    }

    public static void backtracking(int now_row, long slash, long r_slash, int column){
        if(now_row == N){
            result++;
            return;
        }

        for(int col=0; col<N; col++){
            if((column & (1<<col)) != 0 ){
                continue;
            }

            if((slash & (1<<(now_row - col + N))) != 0 ){
                continue;
            }

            if((r_slash & (1<<(now_row + col))) != 0 ){
                continue;
            }


            backtracking(now_row+1,slash | 1<<(now_row - col + N), r_slash | (1<<(now_row + col)) ,column | 1<<col);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());        

        // 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수 출력
        backtracking(0, 0, 0,0);
        System.out.println(result);
    }
}



// 못 놓는 곳들을 마킹?

// 1 0 0 0 
// 0 0 0 0
// 0 1 0 0 
// 0 0 0 1