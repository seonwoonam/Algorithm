import java.util.*;
/**
 * N 명의 선수들이 경기 진행
 * 
 * L 개로 리그가 나눠짐( 0 ~ L-1)
 * - ID 값이 작을수록 우수한 리그
 * 
 * N명의 선수(0 ~ N-1)
 *  - ID 값을 갖고 있고
 *  - 각각의 능력 값을 갖고 있음
 *  - 선수의 능력은 능력 값과 ID값으로 평가
 * 
 *  - 능력값이 높을수록 좋은선수, 능력 값이 같다면 ID가 작을수록 더 능력이 좋은 선수
 * 
 * 제약조건
 * - N은 L의 배수
 * - N/L은 홀수 값을 갖는다. 
 * 
 * 승강제
 * - 각 리그에서 능력이 가장 좋지 않는 선수는 바로 아래리그로 내려가고
 * - 리그에서 가장 능력이 좋은 선수는 바로 위 리그로 올라간다. 
 * 
 * - 이동하는 선수 :  (L-1)*2 명
 * - 맨뒤와 맨앞은 이동하지 않음
 * 
 * - 이동한 선수들의 id값?
 * 
 * 트레이드 제도
 * - 각각의 리그에서 능력이 가장 좋은 선수를 바로 위 리그의 중간급 능력의 선수와 맞교환
 * - 리그 내에 M명이 존재할 때, (M+1) / 2 번째 능력이 좋은 선수
 * 
 * - 이동한 선수들의 id값?
 */

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
    People[][] p_arr;
    int per_people;
    int team_count;


    void init(int N, int L, int mAbility[]) {
        // N < 40,000
        // L < 10
        // 3 ≤ N / L ≤ 3,999
        // 능력치 최대 <= 10,000
        // 앞 번호 리그부터 선수들의 ID 순서대로 N/L명씩 차례대로 배치
        p_arr = new People[L][N/L];
        int id = 0;
        for(int i=0; i<L; i++){
            for(int j=0; j<N/L; j++){
                p_arr[i][j] = new People(id,mAbility[id]);
                id++;
            }
        }

        for(int i=0; i<L; i++){
            Arrays.sort(p_arr[i]);
        }

        this.per_people = N/L;
        this.team_count = L;

    }

    int move() {
        // - 각 리그에서 능력이 가장 좋지 않는 선수는 바로 아래리그로 내려가고
        // - 리그에서 가장 능력이 좋은 선수는 바로 위 리그로 올라간다. 
        // return 이동한 선수들의 ID값의 합
        // 최대 500회 호출 
        // 10^5 이내
        int result = 0;
        HashSet<People> set = new HashSet<>();

        for(int i=0; i< this.team_count-1; i++){
            People temp = p_arr[i][this.per_people-1];
            p_arr[i][this.per_people-1] = p_arr[i+1][0];
            p_arr[i+1][0] = temp;
            set.add(p_arr[i][this.per_people-1]);
            set.add(p_arr[i+1][0]);
        }

        for(int i=0; i< this.team_count; i++){
            Arrays.sort(p_arr[i]);
        }

        for (People p : set) {
            result += p.id;
        }
        

        return result;
    }

    int trade() {
        //- 각각의 리그에서 능력이 가장 좋은 선수를 바로 위 리그의 중간급 능력의 선수와 맞교환
        //  - 리그 내에 M명이 존재할 때, (M+1) / 2 번째 능력이 좋은 선수
        // 최대 1000회 호출
        // 10^5 이내
        int result = 0;
        HashSet<People> set = new HashSet<>();
        
        for(int i=1; i<this.team_count; i++){
            People temp = p_arr[i][0];
            p_arr[i][0] = p_arr[i-1][((this.per_people+1)/2)-1];
            p_arr[i-1][((this.per_people+1)/2)-1] = temp;
            set.add(p_arr[i][0]);
            set.add(p_arr[i-1][((this.per_people+1)/2)-1]);
        }
        
        for(int i=0; i< this.team_count; i++){
            Arrays.sort(p_arr[i]);
        }

        for (People p : set) {
            result += p.id;
        }

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

// 시간복잡도 줄이기.
// 