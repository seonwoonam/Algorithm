import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;

/*
 * 9:40
 * 민트 초코 우유
 * 
 * N*N 크기의 책상 배열. 
 * 각 책상에는 한 명의 학생이 앉아있으며, 총 N^2 명의 학생으로 이루어져있다.
 * 각 학생은 처음에 민트, 초코, 우유 중 하나의 음식만 신봉
 * T : 민트, C : 초코, M : 우유
 * 
 * 다른 사람의 영향을 받음에 따라 다른 종류, 심지어 조합을 신봉하는 학생도 생길 수 있음
 * 
 * 입력
 * - 각 학생은 초기 신앙심을 갖고 있으며, i행j열 학생의 신앙심 주어짐
 * - 이후 T일 동안, 하루는 아침, 점심, 저녁 순서로 아래와 같은 과정 진행된다.
 * 
 * 1. 아침 시간
 * - 모든 학생은 신앙심 1씩 얻음
 * 
 * 2. 점심 시간
 * - 학생들은 인접한 학생들과 신봉 음식이 완전히 같은 경우 그룹을 형성(인접 위치는 상, 하,좌, 우)
 * - 그룹 내에서는 대표자 한 명을 선정. 
 * - 대표자 선정 기준
 * 	- 신앙심이 가장 큰 사람
 *  - 동일할 경우, 행이 가장 작은 사람
 *  - 동일할 경우, 열이 가장 작은 사람
 * - 대표자를 제외한 그룹원들은 각자 신앙심을 1씩 대표자에게 넘김
 * 	- 대표자의 신앙심은 그룹원 수 -1 만큼 추가되고, 나머지는 1씩 감소
 * 
 * 3. 저녁시간
 * - 대표자들이 신앙을 전파
 * - 전파는 그룹 순서가 있음
 * 	- 단일 -> 이중 -> 삼중
 * - 같은 그룹내에서는
 * 	- 대표자의 신앙심이 높은 순
 *  - 동일할 경우 대표자의 행이 가장 작은 사람
 *  - 여전히 동일할 경우 대표자의 열 번호가 작은 순
 *  
 *  파워 : 전파자는 신앙심 B 중 1만 남기고 나머지를 간절함 B-1로 바꿔 전파에 사용
 *  방향 : B를 4로 나눈 나머지 (위, 아래, 왼쪽, 오른쪽)
 *  진행 : 격자 밖으로 나가거나, 파워가 0이 되면 전파는 종료
 *  - 신봉 음식이 같은 경우 전파를 하지 않고 다음으로 진행
 *  - 음식이 다른 경우
 *  	- x>y이면 강한 전파에 성공
 *  		- 완전히 동화됨. 
 *  		- 전파자는 간절함이 (y+1) 만큼 깎인다. 전파 대상의 신앙심은 1증가하게 된다. 
 *  		- 간절함이 0이 되면 더 이상 전파를 하지 않고 종료
 *  	- x<=y 이면 약한 전파에 성공
 *  		- 전파 대상은 전파자가 전파한 음식의 모든 기본 음식에도 관심
 *  		- 기존에 관심을 갖고 있던 음식과 전파자가 관심을 갖고 있는 기본 음식을 모두 합친 음식을 신봉
 *  		- 전파자는 간절함이 0이되고 더 이상 전파를 진행하지 않는다.
 *  		- 대상의 신앙심은 x만큼 증가한다.
 *  
 *  4. 기타
 *  - 어떤 학생(대표자)이 다른 음식의 대표자에게 전파를 당했다면, 그 당일에는 전파를 하지 않는다
 *  - 방어 상태가 되더라고 전파를 받는 거는 가능하다. 
 *  
 * 
 * 
 */
import java.io.*;
import java.util.*;

public class Main {
	static int N, T;
	static HashSet<Character>[][] like_food;
	static int[][] power;
	static int[] dr = {-1,1,0,0};
	static int[] dc = {0,0,-1,1};
	static PriorityQueue<King> king_que;
	static boolean[][] attacked_arr;
	
	public static class King implements Comparable<King>{
		HashSet<Character> food;
		int row;
		int col;
		int pow;
		King(HashSet<Character> food, int row, int col, int pow) {
			this.food = food;
			this.row = row;
			this.col = col;
			this.pow = pow;
		}
		@Override
		public int compareTo(King o) {
			if(this.food.size() == o.food.size()) {
				if(this.pow == o.pow) {
					if(this.row == o.row) {
						return this.col - o.col;
					}
					return this.row - o.row;
				}
				return o.pow - this.pow;
			}
			return this.food.size() - o.food.size();
		}
		
		@Override
		public String toString() {		
			return "["+ this.row + " " + this.col + " " + this.pow + "]";
		}
	}
	
//	 1. 아침 시간
//	 - power에 +1 하기 V
	public static void morning() {
		for(int row=0; row<N; row++) {
			for(int col=0; col<N; col++) {
				power[row][col] += 1;
			}
		}
	}
	
//	 2. 점심시간
//	 - 그루핑 배열이 필요할듯 V
		// group id는 1부터 V
//	 - 그룹 형성하기(BFS) V
//	 	- 대표도 함께 선정 V
//	 	- 대표 리스트에 저장 V
//	 	- 우선순위 큐에 대표들 저장 V
//	 * - 대표자를 제외한 그룹원들은 각자 신앙심을 1씩 대표자에게 넘김 V
//	 * 	- 대표자의 신앙심은 그룹원 수 -1 만큼 추가되고, 나머지는 1씩 감소 V
	
	public static boolean in_range(int row, int col) {
		return 0<=row && row<N && 0<=col && col<N;
	}
	
	public static void bfs(int[][] group_arr, int group_id, int row, int col) {
		HashSet<Character> now_char = like_food[row][col];
		Queue<int[]> que = new ArrayDeque<>();
		int count = 0;
		
		que.offer(new int[] {row, col});
		group_arr[row][col] = group_id;

        // new HashSet으로 안하면 likef_food[row][col]의 값이 바뀌었는데, king의 값도 연달아 바뀌는 문제가 생길 수 있다.
		King ki = new King(new HashSet<>(now_char), row, col, power[row][col]);
		
		while(!que.isEmpty()) {
			int[] now = que.poll();
			count += 1;
			for(int k=0; k<4; k++) {
				int next_row = now[0] + dr[k];
				int next_col = now[1] + dc[k];
				
				if(in_range(next_row, next_col) && group_arr[next_row][next_col] == 0 && now_char.equals(like_food[next_row][next_col])) {
					que.offer(new int[] {next_row, next_col});
					group_arr[next_row][next_col] = group_id;
					King temp = new King(new HashSet<>(now_char), next_row, next_col, power[next_row][next_col]);
					
					if(temp.compareTo(ki) < 0) {
						ki = temp;
					}
				}
			}
		}
		
		// 대표
		for(int r=0; r<N; r++) {
			for(int c=0;c<N; c++) {
				if(group_arr[r][c] != group_id) continue; 
				
				if(ki.row == r && ki.col == c) {
					power[r][c] += (count - 1);
					// 이거 빠뜨릴뻔
					ki.pow += (count-1);
				}else {
					power[r][c] -= 1;
				}
			}
		}
		
		king_que.offer(ki);
	}
	
	public static void lunch() {
		int[][] group_arr = new int[N][N];
		int group_id = 1;
		king_que = new PriorityQueue<>();
		
		for(int row=0; row<N; row++) {
			for(int col=0; col<N; col++) {
				if(group_arr[row][col] != 0) continue;
				bfs(group_arr, group_id++, row, col);
			}
		}
	}
	
	
//	 *  3. 저녁시간
//	 *  - 대표(음식 {}, 대표자 r, 대표자 c, 신앙심)
//	 *  - 우선순위 큐에 대표들 넣어서 
//	 *  - 시뮬레이션 구현
//	 *  	- 신앙심이 0이 될때까지 while 반복
	
//	 *  파워 : 전파자는 신앙심 B 중 1만 남기고 나머지를 간절함 B-1로 바꿔 전파에 사용 v
//	 *  방향 : B를 4로 나눈 나머지 (위, 아래, 왼쪽, 오른쪽) v 
//	 *  진행 : 격자 밖으로 나가거나, 파워가 0이 되면 전파는 종료 v
//	 *  - 신봉 음식이 같은 경우 전파를 하지 않고 다음으로 진행 V
//	 *  - 음식이 다른 경우
//	 *  	- x>y이면 강한 전파에 성공
//	 *  		- 완전히 동화됨. v
//	 *  		- 전파자는 간절함이 (y+1) 만큼 깎인다. 전파 대상의 신앙심은 1증가하게 된다. v
//	 *  		- 간절함이 0이 되면 더 이상 전파를 하지 않고 종료 v
//	 *  	- x<=y 이면 약한 전파에 성공
//	 *  		- 전파 대상은 전파자가 전파한 음식의 모든 기본 음식에도 관심 v
//	 *  		- 기존에 관심을 갖고 있던 음식과 전파자가 관심을 갖고 있는 기본 음식을 모두 합친 음식을 신봉 v
//	 *  		- 전파자는 간절함이 0이되고 더 이상 전파를 진행하지 않는다. v
//	 *  		- 대상의 신앙심은 x만큼 증가한다. v
//	 *  
//	 *  4.기타 V
//	 *  - 공격 당함을 체크해놓는 2차원 배열 필요함 V
//	 *  - 그리고 공격하기 전 대표가 공격받은 애인지 확인하기 V
	
	public static void dinner() {
		attacked_arr = new boolean[N][N];
		while(!king_que.isEmpty()) {
			King king = king_que.poll();	
			// 건너뛰기
			if(attacked_arr[king.row][king.col]) {
				continue;
			}
			
			
			int power_jeonpa = king.pow - 1;
			int dir_jeonpa = king.pow % 4; 
			int now_jeonpa_row = king.row + dr[dir_jeonpa];
			int now_jeonpa_col = king.col + dc[dir_jeonpa];
			
			// 시뮬레이션 구현
			while(power_jeonpa >0 && in_range(now_jeonpa_row, now_jeonpa_col)) {
				if(king.food.equals(like_food[now_jeonpa_row][now_jeonpa_col])) {
					now_jeonpa_row = now_jeonpa_row + dr[dir_jeonpa];
					now_jeonpa_col = now_jeonpa_col + dc[dir_jeonpa];
					continue;
				}
				
				if(power_jeonpa > power[now_jeonpa_row][now_jeonpa_col]) {
					// 강한 전파
					like_food[now_jeonpa_row][now_jeonpa_col] = new HashSet<>(king.food);
					power_jeonpa -= (power[now_jeonpa_row][now_jeonpa_col] + 1);
					power[now_jeonpa_row][now_jeonpa_col] += 1;
				}else {
					// 약한 전파
					like_food[now_jeonpa_row][now_jeonpa_col].addAll(new HashSet<>(king.food));
					power[now_jeonpa_row][now_jeonpa_col] += power_jeonpa;
					power_jeonpa = 0;
				}
				
				// 전파 계속
				attacked_arr[now_jeonpa_row][now_jeonpa_col] = true;
				now_jeonpa_row = now_jeonpa_row + dr[dir_jeonpa];
				now_jeonpa_col = now_jeonpa_col + dc[dir_jeonpa];
			}
				
			// 전체 업데이트
			// king은 신앙심 1만 남겨야함
			power[king.row][king.col] = 1;
	
		}
	}
	
//	 *  5. 출력
//	 *  - 신앙심 총합 구하기
//	 *  - HashMap<HashSet, Integer> 활용
	public static void result() {
		HashMap<HashSet, Integer> result = new HashMap<>();
		HashSet<Character> first = new HashSet<>();
		HashSet<Character> second = new HashSet<>();
		HashSet<Character> third = new HashSet<>();
		HashSet<Character> fourth = new HashSet<>();
		HashSet<Character> fifth = new HashSet<>();
		HashSet<Character> sixth = new HashSet<>();
		HashSet<Character> seventh = new HashSet<>();
		
		first.add('T');
		first.add('C');
		first.add('M');
		
		second.add('T');
		second.add('C');
		
		third.add('T');
		third.add('M');
		
		fourth.add('C');
		fourth.add('M');
		
		fifth.add('M');
		
		sixth.add('C');
		
		seventh.add('T');
		
		result.put(first, 0);
		result.put(second, 0);
		result.put(third, 0);
		result.put(fourth, 0);
		result.put(fifth, 0);
		result.put(sixth, 0);
		result.put(seventh, 0);
		
		
		for(int row=0; row<N; row++) {
			for(int col=0; col<N; col++) {
				result.put(like_food[row][col], result.get(like_food[row][col])+power[row][col]);
			}
		}
		
		System.out.println(result.get(first) + " " + result.get(second) + " " + result.get(third) + " " + result.get(fourth) + " " + result.get(fifth) + " " + result.get(sixth) + " " + result.get(seventh));
	}
	
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	
    	st = new StringTokenizer(br.readLine());
    	N = Integer.parseInt(st.nextToken());
    	T = Integer.parseInt(st.nextToken());
    	like_food = new HashSet[N][N];
    	power = new int[N][N];
    	for(int row=0; row<N; row++) {
    		String string = br.readLine();
    		for(int col=0; col<N; col++) {
    			like_food[row][col] = new HashSet<>();
    			like_food[row][col].add(string.charAt(col));
    		}
    	}
    	for(int row=0; row<N; row++) {
    		st = new StringTokenizer(br.readLine());
    		for(int col=0; col<N; col++) {
    			power[row][col] = Integer.parseInt(st.nextToken());
    		}
    	}
    	
    	for(int time=1; time<= T; time++) {
    		morning();
    		lunch();
    		dinner();
    		result();
//    		System.out.println("===========");
//    		System.out.println(Arrays.deepToString(power));
//    		System.out.println(king_que.toString());
    	}
    }
}

//System.out.println(Arrays.deepToString(like_food));
//System.out.println(Arrays.deepToString(power));

//for(int row=0; row<N; row++) {
//	for(int col=0; col<N; col++) {
//		
//	}
//}


