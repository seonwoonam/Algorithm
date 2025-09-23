
/*
    9:36 ~ 
    
    N*N 크기의 정사각형 형태의 배양용기
    - 좌측 하단 (0,0) 우측 상단 (N, N)
    N <= 15
    Q <= 50

    총 Q번의 실험을 진행하며 각 실험의 결과 기록
    
    실험
    1. 미생물 투입
    - 좌측 하단 좌표가 (r1, c1)이고 우측 상단 좌표 (r2, c2) 직사각형 영역에 한 무리의 미생물
    - 만약에 다른 미생물이 존재한다면, 덮어씌움
    - 만약 기존에 있던 어떤 미생물 무리 A가 B에게 잡아먹히면서 둘 이상으로 나누어지게 되면, A무리의 
        미생물은 모두 사라진다 ===> 한 군집으로 보는것을 찾아야 할듯(BFS)
    
    2. 배양 용기 이동
    - 모든 미생물을 새로운 배양 용기로 
    - 이 과정은 기존 배양 용기에 미생물이 한 마리도 존재하지 않을 때 까지 다음 작업 반복
        반복
        - 기존배양 용기 중 가장 차지한 영역이 넓은 무리 하나를 선택
        - 만약 무리가 둘 이상이면 가장 먼저 투입된 미생물 선택
        - 선택된 미생물 무리를 새 배양 용기에 옮기기
            - 이때 형태 유지
            - 다른 미생물 영역과 겹치지 않게 두기
            - 이 조건안에서 최대한 x좌표가 작은 위치로
                - 그런 좌표 둘 이상이면 y 좌표가 작은 위치로
        - 옮기는 과정에서 어떤 곳도 놓을 수 없는 경우 버려짐
    
    3. 실험 결과 기록
    - 미생물 무리 중 상하좌우로 맞닿은 면이 있는 무리끼리는 인접한 무리라고 표현
    - 모든 인접한 무리 쌍 확인
        - A 넓이 * B 넓이 만큼의 성과 얻음
    - 확인한 모든 쌍의 성과를 더한 값이 결과이다. 

    후기 
    - 복제하는 아이디어를 떠올리는데 어려웠다.
    - 구현 꼼꼼하게
    - 복잡한 디버깅을 잘하는 방법??
    - i,j같은 걸 헷갈리지 않게 단어로
*/
import java.io.*;
import java.util.*;

public class Main {
    static int N; 
    static int Q;
    // index = 0이면 지워진거
    static int index = 1;
    static Mesang[] mesang_arr;
    static int[][] map;
    static int[] dy = {1, 0, 0 ,-1};
    static int[] dx = {0, 1, -1, 0};
    

    public static class Mesang implements Comparable<Mesang>{
        int id;
        int count;
        Mesang(int id, int count){
            this.id = id;
            this.count = count;
        }
        @Override
        public int compareTo(Mesang o){
            if(this.count == o.count){
                return this.id - o.id;
            }
            return o.count - this.count;
        }
    }

    public static boolean in_range(int r, int c){
        return 0<=r && r<N && 0<=c && c<N;
    }

    public static int bfs(int index){
        Queue<int[]> que = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][N];
        int start_y = -1;
        int start_x = -1;
        outer:
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(map[i][j] == index){
                   start_y = i;
                   start_x = j;
                   break outer;
                }
            }
        }
        if(start_y == -1 && start_x == -1){
            return 0;
        }
        que.offer(new int[]{start_y, start_x});
        visited[start_y][start_x] = true; 
        int cnt = 1;
        while(!que.isEmpty()){
            int[] now = que.poll();
            for(int k=0; k<4; k++){
                int next_y = now[0] + dy[k];
                int next_x = now[1] + dx[k];
                if(in_range(next_y, next_x) && !visited[next_y][next_x] && map[next_y][next_x] == index){
                    cnt++;
                    que.offer(new int[]{next_y, next_x});
                    visited[next_y][next_x] = true;
                }
            }
        }
        return cnt;
    }

    // 1. 미생물 투입
    // - 미생물 클래스 필요 (id, 미생물 개수) v
    // - 받은 위치에 미생물 ID 넣기 v
    // - 들어간 미생물을 담아서 관리하는 자료구조 필요 v
    // - 다른 미생물 존재 시 덮어 씌움 v
    // - 둘 이상으로 나눠지면 삭제 시킴 v
    //     - 어떻게 갈라진지 아냐?(카운트하는 변수 필요) v
    //     - BFS 활용 v
    public static void insert(int x1, int y1, int x2, int y2){
        int count = (x2 - x1) * (y2 - y1);
        Mesang m = new Mesang(index, count);
        mesang_arr[index] = m;
        // treeset.add(m);

        HashSet<Integer> temp = new HashSet<>();
        for(int i=y1; i<y2; i++){
            for(int j=x1; j<x2; j++){
                if(map[i][j] != 0){
                    temp.add(map[i][j]);
                    mesang_arr[map[i][j]].count -= 1;
                }
                map[i][j] = index;
            }
        }

        // 갈라진 지 확인하기
        for(int idx : temp){
            Mesang now_m = mesang_arr[idx];
            int c = bfs(now_m.id);

            if (now_m.count == 0 && c == 0) {
                now_m.id = 0; 
                now_m.count = 0;
                continue;
            }

            // 삭제 조치
            if(c!=now_m.count){
                for(int i=0; i<N; i++){
                    for(int j=0; j<N; j++){
                        if(map[i][j] == now_m.id){
                            map[i][j] = 0;
                        }
                    }
                }
                now_m.count = 0;
                now_m.id = 0;
            }
        }
        index++;
    }

    // 2. 배양 용기 이동
    // - index = 0이면 지워진거 v
    // - PQ에서 가져올 미생물 군집 빼오기 v
    // - 고민
    //     - 형태를 어떻게 유지? v
    //         - 상대 위치를 사용한다. v
    //     - 다른 미생물과 안겹치게?
    //         - 잘린거가 있어서 범위 파악으로는 안될거다 v
    //         - 직접 넣어보는 방법 => 시간복잡도 괜찮을듯 v
    //
    //     - 이 조건안에서 최대한 x좌표가 작은 위치로 v
    //         - 그런 좌표 둘 이상이면 y 좌표가 작은 위치로 v
    //      열 먼저보기 v
    //     - 어떠한 곳에도 못넣으면 버려야 하는데? v
    public static void move(){
        int[][] temp = new int[N][N];
        PriorityQueue<Mesang> pq = new PriorityQueue<>();
        for(int i=1; i<Q+1;i++){
            if(mesang_arr[i] == null) break;
            Mesang m = mesang_arr[i];
            if (m.id == 0 || m.count == 0) continue;
            pq.offer(m);
        }

        while(!pq.isEmpty()){
            Mesang now = pq.poll();

            int min_r = -1, min_c = -1;
            boolean anchorFound = false;
            for (int i = 0; i < N; i++) { 
                for (int j = 0; j < N; j++) { 
                    if (map[j][i] == now.id) {
                        min_r = j;
                        min_c = i;
                        anchorFound = true;
                        break; 
                    }
                }
                if (anchorFound) {
                    break; 
                }
            }

            if(!anchorFound) continue;
            ArrayList<int[]> move_list = new ArrayList<>();
            for(int i=0; i<N; i++){
                for(int j=0; j<N; j++){
                    if(map[j][i] == now.id){
                        move_list.add(new int[]{j - min_r, i-min_c});
                    }
                }
            }

            // 배치하기
            boolean change = false;
            for(int i=0; i<N; i++){
                for(int j=0; j<N; j++){
                    
                    boolean find = true;
                    for(int[] check : move_list){
                        if(in_range(j+check[0], i+check[1]) && temp[j+check[0]][i+check[1]] == 0){
                            continue;
                        }else{
                            find = false;
                            break;
                        }
                    }

                    if(find){
                        change = true;
                        for(int[] check : move_list){
                            if(in_range(j+check[0], i+check[1]) && temp[j+check[0]][i+check[1]] == 0){
                                temp[j+check[0]][i+check[1]] = now.id;
                            }
                        }

                        break;
                    }
                }
                if(change){
                    break;
                }
            }

            // 어디에도 들어가지 못하면 버려주기
            if(!change){
                now.id = 0;
                now.count = 0;
            }
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N;j++){
                map[i][j] = temp[i][j];
            }
        }
    }

    //  3. 실험 결과 기록
    // - 미생물이 위치하는 곳부터 BFS 돌리기
    // - 다른 아이디 처음 방문이면 곱하기
    public static void result() {
        boolean[][] adj = new boolean[Q + 1][Q + 1];
        int ans = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                int a = map[r][c];
                if (a == 0) continue;

                for (int k = 0; k < 4; k++) {
                    int nr = r + dy[k];
                    int nc = c + dx[k];
                    if (!in_range(nr, nc)) continue;
                    int b = map[nr][nc];
                    if (b == 0 || a == b) continue;

                    if (!adj[a][b]) {
                        adj[a][b] = adj[b][a] = true;
                    }
                }
            }
        }

        // 인접쌍의 곱 합산 (중복 방지: a<b)
        for (int a = 1; a <= Q; a++) {
            if (mesang_arr[a] == null || mesang_arr[a].id == 0 || mesang_arr[a].count == 0) continue;
            for (int b = a + 1; b <= Q; b++) {
                if (!adj[a][b]) continue;
                if (mesang_arr[b] == null || mesang_arr[b].id == 0 || mesang_arr[b].count == 0) continue;
                ans += mesang_arr[a].count * mesang_arr[b].count;
            }
        }

        System.out.println(ans);
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        int[][] arr = new int[Q][4];
        mesang_arr = new Mesang[Q+1];
        map = new int[N][N];
        for(int i=0; i<Q; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<4;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i<Q; i++){
            insert(arr[i][0], arr[i][1], arr[i][2], arr[i][3]);
            move();
            // System.out.println(Arrays.deepToString(map));
            result();
        }
    }
}