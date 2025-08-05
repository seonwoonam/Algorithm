import java.io.*;
import java.util.*;

// 유형 : 단순 구현
// 주의할 점
// 반시계로 돌아가면서 이미 확인해서 겹치는 부분은 제외해줘야 한다. 

// 구현부
// 1. 각각의 껍질 구분해주기
// 2. 일렬로 나열
// 3. 나머지 연산을 통해 변경
// 4. 정렬
// 5. 다시 배열 채우기
// 6. 출력

class Main{    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        String line = br.readLine();
        st = new StringTokenizer(line);
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        
        int[][] arr = new int[N][M];
        int[][] result = new int[N][M];
        
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                arr[i][j] =  Integer.parseInt(st.nextToken());
            }
        }
                
        int ROW_ZERO = 0;
        int COL_ZERO = 0;
        int ROW_END = N-1;
        int COL_END = M-1;
        
        // {값, 순서}
        List<List<int[]>> order_list = new ArrayList<>();
        int order = 0;
        while(ROW_ZERO < ROW_END && COL_ZERO < COL_END){
            List<int[]> new_order = new ArrayList<>();
            for(int i=ROW_ZERO; i<=ROW_END; i++){
                new_order.add(new int[]{ arr[i][COL_ZERO], order++});
            }
            
            for(int i=COL_ZERO+1; i<=COL_END; i++){
                new_order.add(new int[]{arr[ROW_END][i], order++});
            }
            
            for(int i=ROW_END-1; i>=ROW_ZERO; i--){
                new_order.add(new int[]{arr[i][COL_END], order++});
            }
            
            for(int i=COL_END-1; i>=COL_ZERO+1; i--){
                new_order.add(new int[]{arr[ROW_ZERO][i], order++});
            }
            
            order_list.add(new_order);
            
            ROW_ZERO += 1;
            COL_ZERO += 1;
            ROW_END -= 1;
            COL_END -= 1;
            order = 0;
        }
        
        for(int i=0; i < order_list.size(); i++){
            List<int[]> now_order = order_list.get(i);
            int now_size = now_order.size();
            for(int j = 0; j < now_size; j++){
                now_order.get(j)[1] = (now_order.get(j)[1] + R) % now_size;
            }
            now_order.sort((a,b) -> a[1]-b[1]);
        }
        
        ROW_ZERO = 0;
        COL_ZERO = 0;
        ROW_END = N-1;
        COL_END = M-1;
        
        // {값, 순서}
        int now_index = 0;
        while(ROW_ZERO < ROW_END && COL_ZERO < COL_END){
            List<int[]> now_order = order_list.get(now_index++);
            int index = 0;
        
            for(int i=ROW_ZERO; i<=ROW_END; i++){
                result[i][COL_ZERO] = now_order.get(index++)[0];
            }
            
            for(int i=COL_ZERO+1; i<=COL_END; i++){
                result[ROW_END][i] = now_order.get(index++)[0];
            }
            
            for(int i=ROW_END-1; i>=ROW_ZERO; i--){
                result[i][COL_END] = now_order.get(index++)[0];
            }
            
            for(int i=COL_END-1; i>=COL_ZERO+1; i--){
                result[ROW_ZERO][i] = now_order.get(index++)[0];
            }

            ROW_ZERO += 1;
            COL_ZERO += 1;
            ROW_END -= 1;
            COL_END -= 1;
        }
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}