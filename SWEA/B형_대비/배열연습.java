import java.io.*;
import java.util.StringTokenizer;

import javax.print.DocFlavor.CHAR_ARRAY;

/**
 * 그냥 br.readLine() 이면 trim 필요할 때도 있음
 * StringTokenizer 사용시에는 trim 필요없음
 * 
 * 1. x 탐색 혹은, + 방향 탐색은 dx, dy 테크니션을 사용하는게 편하다.
 */

class Solution_배열연습
{
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // 공백 있으면 StringTokenizer가 편할듯.
    static StringTokenizer st;
    static StringBuilder sb;
    static public boolean in_range(int r,int c,int N,int M){
        return 0<=r & r<N & 0<=c & c<M;
    }
    public static void main(String args[]) throws Exception
	{
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        /* 입력 */
        char[][] arr = new char[N][M];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                arr[i][j] = st.nextToken().charAt(0);
            }
        }

        // 지그재그 탐색
        sb = new StringBuilder();
        for(int i=0;i<N;i++){
            if(i%2==0){
                for(int j=0; j<M; j++){
                    sb.append(arr[i][j]);
                }
            }

            if(i%2==1){
                for(int j=M-1; j>=0;j--){
                    sb.append(arr[i][j]);
                } 
            }
        }
        System.out.println(sb);

        // 모음의 주변을 x로 탐색하고 요소의 합 출력
        int[] dr = {-1, -1, 1, 1};
        int[] dc = {-1, 1, 1, -1};
        int sum = 0;
        for(int i=0; i<N;i++){
            for(int j=0; j<M; j++){
                if("AEIOU".indexOf(arr[i][j]) != -1){
                    for(int k = 0; k<4;k++){
                        if(in_range(i+dr[k],j+dc[k],N,M)){
                            sum = sum + (arr[i+dr[k]][j+dc[k]] - 'A');
                        }
                    }
                }

            }
        }
        System.out.print(sum);

 
        /* 출력 */
        // sb = new StringBuilder();
        // for(int i=0;i<N;i++){
        //     for(int j=0;j<N;j++){
        //         sb.append(arr[i][j]).append(" ");
        //     }
        //     // bw.write(sb.toString().trim());
        //     // bw.newLine();
        //     sb.append('\n');
        // }
        // // bw.flush();
        // System.out.println(sb);
    }
}