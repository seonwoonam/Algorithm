import java.io.*;
import java.util.*;

class Main{
    static int[] dr = {0,0,1,-1};
    static int[] dc = {1,-1,0,0};
    static int[][] arr;

    public static boolean in_range(int r, int c, int N, int M){
        return 0<=r && r<N && 0<=c && c<M;
    }

    // visited check 언제 해야하는가?
    // 뚫게 하는거를 어떻게 할것인가?
    // visited의 차원을 늘려서 해결!!

    public static void bfs(int N, int M){
        int[][][] visited = new int[N][M][2];
        Queue<int[]> que = new ArrayDeque<>();
        que.offer(new int[]{0,0,0});
        visited[0][0][0] = 1;

        while(!que.isEmpty()){
            int[] now = que.poll();
            int now_r = now[0];
            int now_c = now[1];
            int wall = now[2];
            
            if(now_r == N-1 && now_c == M-1){
                System.out.println(visited[now_r][now_c][wall]);
                return;
            }
            
            for(int k=0; k<4; k++){
                int next_r = now_r + dr[k];
                int next_c = now_c + dc[k];

                if(!in_range(next_r, next_c, N, M)){
                    continue;
                }

                if(visited[next_r][next_c][wall] != 0){
                    continue;
                }

                if(arr[next_r][next_c] == 1){
                    if(wall == 0){
                        que.offer(new int[]{next_r, next_c, 1});
                        visited[next_r][next_c][wall+1] = visited[now_r][now_c][wall] + 1;
                    }
                }else{
                    que.offer(new int[]{next_r, next_c,wall});
                    visited[next_r][next_c][wall] = visited[now_r][now_c][wall] + 1;
                }
            }
        }
        System.out.println(-1);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];

        for(int i=0; i<N;i++){
            String str = br.readLine();
            for(int j=0;j<M;j++){
                arr[i][j] = str.charAt(j) - '0';
            }
        }
        bfs(N,M);
    }
}