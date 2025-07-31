import java.util.*;

class 승강제리그 {
    private static Scanner sc;
    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT = 100;
    private final static int CMD_MOVE = 200;
    private final static int CMD_TRADE = 300;

    private static boolean run() throws Exception {

        int query_num = sc.nextInt();
		int ans;
        boolean ok = false;

        for (int q = 0; q < query_num; q++) {
            int query = sc.nextInt();

            if (query == CMD_INIT) {
                int N = sc.nextInt();
                int L = sc.nextInt();
                int mAbility[] = new int[N];
                for (int i = 0; i < N; i++){
                    mAbility[i] = sc.nextInt();
                }
                usersolution.init(N, L, mAbility);
                ok = true;
            } else if (query == CMD_MOVE) {
                int ret = usersolution.move();
                ans = sc.nextInt();
                if (ans != ret) {
                    ok = false;
                }
            } else if (query == CMD_TRADE) {
                int ret = usersolution.trade();
                ans = sc.nextInt();
                if (ans != ret) {
                    ok = false;
                }
            }
        }
        return ok;
    }

    public static void main(String[] args) throws Exception {
        int T, MARK;

        System.setIn(new java.io.FileInputStream("sample_input.txt"));
        sc = new Scanner(System.in);
        T = sc.nextInt();
        MARK = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int score = run() ? MARK : 0;
            System.out.println("#" + tc + " " + score);
        }
        sc.close();
    }
}

class UserSolution {
    static class People implements Comparable<People>{
        int id;
        int ability;

        public People(int id, int ability) {
            this.id = id;
            this.ability = ability;
        }

        @Override
        public int compareTo(People p){
            if(this.ability > p.ability){
                return -1;

            }else if(this.ability == p.ability){
                if(this.id < p.id){
                    return -1;
                }else{
                    return 1;
                }
            }else {
                return 1;
            }
        }
    }
    // People[][] p_arr;
    int per_people;
    int team_count;
    PriorityQueue<People>[] dsc_queue;
    PriorityQueue<People>[] asc_queue;

    // 중간 윗부분
    PriorityQueue<People>[] middle_acs_queue;
    // 중간 아랫부분
    PriorityQueue<People>[] middle_dsc_queue;

    // asc_queue : (per_people + 1) / 2 개
    // dsc_queue : ((per_people + 1) / 2) - 1개

    void initMiddleQueue(People p, int index){
        if(middle_acs_queue[index].size() >= ((this.per_people + 1)/2)){
            if(middle_acs_queue[index].peek().compareTo(p) > 0){
                // p가 더 크다
                People temp = middle_acs_queue[index].poll();
                middle_dsc_queue[index].offer(temp);
                middle_acs_queue[index].offer(p);
            }else{
                middle_dsc_queue[index].offer(p);
            }
        }else{
            middle_acs_queue[index].offer(p);
        }

    }

    void offerMiddleQueue(People p, int index){
        if(middle_dsc_queue[index].peek().compareTo(p) > 0){
            // p가 더 클때
            middle_acs_queue[index].offer(p);
        }else{
            People temp = middle_dsc_queue[index].poll();
            middle_acs_queue[index].offer(temp);
            middle_dsc_queue[index].offer(p);
        }
    }

    void offer_move_MiddleQueue(People p, int index){
        if(middle_dsc_queue[index].peek() == null || middle_dsc_queue[index].peek().compareTo(p) > 0){
            // p가 더 클때
            if(middle_acs_queue[index].size() >= ((this.per_people + 1) / 2)){
                // 꽉 차있음
                if(middle_acs_queue[index].peek().compareTo(p) > 0){
                    People temp = middle_acs_queue[index].poll();
                    middle_dsc_queue[index].offer(temp);
                    middle_acs_queue[index].offer(p);
                }else{
                    middle_dsc_queue[index].offer(p);
                }
            }else{
                middle_acs_queue[index].offer(p);
            }
        }else{
            // p가 더 작을 때
            if(middle_dsc_queue[index].size() >= ((per_people + 1) / 2) - 1){
                // 꽉 차있음
                People temp = middle_dsc_queue[index].poll();
                middle_acs_queue[index].offer(temp);
                middle_dsc_queue[index].offer(p);
            }else{
                middle_dsc_queue[index].offer(p);
            }
        }
    }


    void init(int N, int L, int mAbility[]) {
        // N < 40,000
        // L < 10
        // 3 ≤ N / L ≤ 3,999
        // 능력치 최대 <= 10,000
        // 앞 번호 리그부터 선수들의 ID 순서대로 N/L명씩 차례대로 배치
        dsc_queue = new PriorityQueue[L];
        asc_queue = new PriorityQueue[L];
        middle_acs_queue = new PriorityQueue[L];
        middle_dsc_queue = new PriorityQueue[L];
        this.per_people = N/L;
        this.team_count = L;

        for(int i=0;i<L;i++){
            dsc_queue[i] = new PriorityQueue<People>();
            asc_queue[i] = new PriorityQueue<People>(Collections.reverseOrder());
            middle_dsc_queue[i] = new PriorityQueue<People>();
            middle_acs_queue[i] = new PriorityQueue<People>(Collections.reverseOrder());
        }

        // p_arr = new People[L][N/L];
        int id = 0;
        for(int i=0; i<L; i++){
            for(int j=0; j<N/L; j++){
                People new_people = new People(id,mAbility[id]);
                dsc_queue[i].offer(new_people);
                asc_queue[i].offer(new_people);
                initMiddleQueue(new_people, i);
                id++;
            }
        }

        // for(int i=0; i<L; i++){
        //     Arrays.sort(p_arr[i]);
        // }
    }

    int move() {
        // - 각 리그에서 능력이 가장 좋지 않는 선수는 바로 아래리그로 내려가고
        // - 리그에서 가장 능력이 좋은 선수는 바로 위 리그로 올라간다. 
        // return 이동한 선수들의 ID값의 합
        // 최대 500회 호출 
        // 10^5 이내
        int result = 0;
        HashSet<People> set = new HashSet<>();
        
        People[] temp_min = new People[this.team_count];
        People[] temp_max = new People[this.team_count];

        // 각 팀의 제일 작은 애들 뽑기
        for(int i=0; i< this.team_count-1;i++){
            temp_min[i] = asc_queue[i].poll();
            dsc_queue[i].remove(temp_min[i]);
            middle_dsc_queue[i].remove(temp_min[i]);
            set.add(temp_min[i]);
        }

        // 각 팀의 제일 큰 애들 뽑기
        for(int i=1; i< this.team_count;i++){
            temp_max[i] = dsc_queue[i].poll();
            asc_queue[i].remove(temp_max[i]);
            middle_acs_queue[i].remove(temp_max[i]);
            set.add(temp_max[i]);
        }

        // 큰 애들 옮기기
        for(int i=0;i<this.team_count-1;i++){
            asc_queue[i].offer(temp_max[i+1]);
            dsc_queue[i].offer(temp_max[i+1]);
            offer_move_MiddleQueue(temp_max[i+1],i);
        }

        // 작은 애들 옮기기
        for(int i=1;i<this.team_count;i++){
            asc_queue[i].offer(temp_min[i-1]);
            dsc_queue[i].offer(temp_min[i-1]);
            offer_move_MiddleQueue(temp_min[i-1],i);
        }

        for (People p : set) {
            result += p.id;
        }

        // 하나, 하나 빔
        return result;
    }

    // 우선순위 큐
    // 중간급을 뽑아내고 다시 넣는게? 
    int trade() {
        //- 각각의 리그에서 능력이 가장 좋은 선수를 바로 위 리그의 중간급 능력의 선수와 맞교환
        //  - 리그 내에 M명이 존재할 때, (M+1) / 2 번째 능력이 좋은 선수
        // 최대 1000회 호출
        // 10^5 이내
        int result = 0;
        HashSet<People> set = new HashSet<>();

        People[] temp_middle = new People[this.team_count];
        People[] temp_max = new People[this.team_count];
        
        // 중간애들 뽑기
        for(int i=0; i< this.team_count-1;i++){
            temp_middle[i] = middle_acs_queue[i].poll();
            asc_queue[i].remove(temp_middle[i]);
            dsc_queue[i].remove(temp_middle[i]);
            set.add(temp_middle[i]);
        }


        // 각 팀의 제일 큰 애들 뽑기
        // 10 * log P
        for(int i=1; i< this.team_count;i++){
            temp_max[i] = dsc_queue[i].poll();
            asc_queue[i].remove(temp_max[i]);
            middle_acs_queue[i].remove(temp_max[i]);
            set.add(temp_max[i]);
        }

        ///

        // 큰 애들 옮기기
        // 10 * log P
        for(int i=0;i<this.team_count-1;i++){
            asc_queue[i].offer(temp_max[i+1]);
            dsc_queue[i].offer(temp_max[i+1]);
            offerMiddleQueue(temp_max[i+1],i);
        }

        // 중간 애들 옮기기
        // 10 * log P
        for(int i=1;i<this.team_count;i++){
            asc_queue[i].offer(temp_middle[i-1]);
            dsc_queue[i].offer(temp_middle[i-1]);
            offerMiddleQueue(temp_middle[i-1],i);
        }

        for (People p : set) {
            result += p.id;
            // System.out.print(p.id + " ");
        }
        // System.out.print('\n');

        return result;
    }

}

// 단순 구현
// 전체 배열에 넣기
// 2차원 배열로 arr[리그][순서] = 사람의 id
// 능력값 어떻게 정렬?
// people class 만들어주기?

// 1차원 배열에 id의 능력치

// P = N / L < 4000

// 10 * 4 * 10^3 * 12 = 약 4 * 10^5
// 각각 그냥 정렬 : 리그 수 * Plog(P)

// (L-1) * 2번 move
// L 만큼 trade

// 약 4 * 10^5 * 10^3 = 4*10^8
// 이렇게 하니까 딱 3004ms 아슬아슬하게 안됨

// 시간복잡도 줄이기.
// 우선순위 큐로 하면 바로 수정이 되어버림. 근데 그러면 안돼.

// compareTo 주의해서 코딩해야할듯.