import java.io.*;
import java.util.*;

public class BJ_14658 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException{
        st = new StringTokenizer(br.readLine());
        int result = 0;

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] arr = new int[K][2];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        for(int i=0; i<K;i++){
            for(int j=0; j<K;j++){
                int now_x = arr[i][0];
                int now_y = arr[j][1];
                int count = 0;
                for(int m=0; m<K; m++){
                    int check_x = arr[m][0];
                    int check_y = arr[m][1];

                    if(now_x <= check_x && check_x <= now_x + L && now_y <= check_y && check_y <= now_y+L){
                        count++;
                    }
                }
                result = Math.max(result, count);
            }
        }
        System.out.println(K-result);
    }
}
