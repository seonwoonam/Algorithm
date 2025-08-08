package swea;

import java.util.*;
import java.io.*;
// 9:15 ~ 10:00
// 루트 노드간의 최단 전송 시간 측정.

// 루트 노드 3개, 최대 300개의 소규모 그룹
// 소규모 그룹
// - 대표노드 3개와 말단노드 최대 27개로 구성되어 있고, 대표 노드 3개는 루트 노드나 다른 그룹의 대표 노드와 연결가능.

// 라인
// - 각각의 라인에는 전송시간이 있다. 
// 최단 전송 시간은 다익스트라 처럼.

// 그룹의 노드 번호 끝단 01,02,03 들이 대표 노드
// % 10?

// 말단 노드들은 내부에서만 서로 연결된다. 

// 네트워크 구성
// 1. 루트 노드는 소규모 대표 노드와만 연결되고, 최대 한 번 연결이다.
// 2. 노드끼리는 서로 최대 한 번 연결이다.
// 3. 소규모 그룹끼리는 소규모 대표 노드를 통해서 최대 한 번 연결이다. 

// 주의
// 라인이 추가되거나 제거될 수 있다.

// 출력
// 루트 노드간의 최단 전송 시간 알아내기


class UserSolution {
	static ArrayList<ArrayList<ArrayList<int[]>>> small_graph;
	static ArrayList<ArrayList<int[]>> large_graph;
	static HashSet<Integer> large_group = new HashSet<>();
	static int NN = 0;
	
	public int[] dijkstra(int find_node, ArrayList<ArrayList<int[]>> graph, int size) {
		int[] distance = new int[size];
		for(int i=0; i<size;i++) {
			distance[i] = 1000000;
		}
		PriorityQueue<int[]> queue = new PriorityQueue<>((a,b)-> a[0]-b[0]);
		
		queue.offer(new int[] {0,find_node});
		distance[find_node] = 0;
		
		while(!queue.isEmpty()) {
			int[] now_val = queue.poll();
			if(now_val[0] > distance[now_val[1]]) {
				continue;
			}else {
				for(int[] next : graph.get(now_val[1])) {
					int next_node = next[0];
					int next_cost = next[1];
					if(distance[next_node] > now_val[0]+next_cost) {
						queue.offer(new int[] {now_val[0]+next_cost, next_node});
						distance[next_node] = now_val[0]+next_cost;
					}
				}
			}
		}
		
		return distance;
	}

	public void init(int N, int K, int mNodeA[], int mNodeB[], int mTime[])
	{
		large_group.clear();
		NN = N;
		large_group.add(1);
		large_group.add(2);
		large_group.add(3);
        // 그냥 최대 노드 개수 : 9,000개
		// 엣지 개수 : 30,000개
        
        // mNodeA, mNodeB 활용해서 그래프 만들기
        // 그래프는 작은 그래프와, 큰 그래프로 나뉘게 됨
		
        // 내부 구성 노드라면 작은 그래프 - 3차원 배열이 될듯 [그룹id][노드id][엣지들]
        	// 굳이 그루핑을 위해 union find 안써도될듯?
       // 대표 노드끼리 이어진 새로운 엣지 제작
		small_graph = new ArrayList<>(N+1);
		for(int i=0;i<N+1;i++) {
			small_graph.add(new ArrayList<>());
		}
		for(int i=0;i<N+1;i++) {
			ArrayList<ArrayList<int[]>> now_group = small_graph.get(i);
			for(int j=0;j<31;j++) {
				now_group.add(new ArrayList<>());
			}
		}		
		ArrayList<int[]> temp_info = new ArrayList<>();
		
		for(int i=0; i<K; i++) {
			int node_A = mNodeA[i];
			int node_B = mNodeB[i];
			int edge = mTime[i];
			
			int idx_A = node_A % 100;
			int idx_B = node_B % 100;
			
			int group_idx_A = node_A / 100;
			int group_idx_B = node_B / 100;
			
			//large_group.contains(idx_A) && large_group.contains(idx_B) && 
			if(group_idx_A != group_idx_B) {
				temp_info.add(new int[]{node_A, node_B, edge});
			}else {
				small_graph.get(group_idx_A).get(idx_A).add(new int[] {idx_B, edge});
				small_graph.get(group_idx_A).get(idx_B).add(new int[] {idx_A, edge});
			}
		}
		
		large_graph = new ArrayList<>(N*100 + 31);
		for(int i=0; i<N*100 + 31; i++) {
			large_graph.add(new ArrayList<>());
		}
		
         // 위에서 만들어진 엣지와 입력데이터를 활용해, 대장 구성들이라면 큰 그래프로 작성 - 2차원 배열 [노드id][엣지들]
		for(int i=0; i<temp_info.size();i++) {
			int[] now_data = temp_info.get(i);
			large_graph.get(now_data[0]).add(new int[]{now_data[1], now_data[2]});
			large_graph.get(now_data[1]).add(new int[]{now_data[0], now_data[2]});
		}
		
		for(int group_idx=1; group_idx<N+1; group_idx++) {
			ArrayList<ArrayList<int[]>> now_graph = small_graph.get(group_idx);
			int[] dist_1 = dijkstra(1, now_graph, 31);
			int[] dist_2 = dijkstra(2, now_graph, 31);
						
			int node_1 = group_idx * 100 + 1;
			int node_2 = group_idx * 100 + 2;
			int node_3 = group_idx * 100 + 3;
			
			large_graph.get(node_1).add(new int[] {node_2, dist_1[2]});
			large_graph.get(node_1).add(new int[] {node_3, dist_1[3]});
			
			large_graph.get(node_2).add(new int[] {node_1, dist_2[1]});
			large_graph.get(node_2).add(new int[] {node_3, dist_2[3]});
			
			large_graph.get(node_3).add(new int[] {node_1, dist_1[3]});	
			large_graph.get(node_3).add(new int[] {node_2, dist_2[3]});
		}
   
	}

	public void addLine(int mNodeA, int mNodeB, int mTime)
	{
        // 최대 200 호출
        // 1. 소규모 그룹 추가
        	// 대표 노드까지의 엣지 수정
		// 2. 대규모 그룹의 엣지 추가
		
		int mNodeA_idx = mNodeA % 100;
		int mNodeB_idx = mNodeB % 100;
		
		int group_idx_A = mNodeA / 100;
		int group_idx_B = mNodeB / 100;
		
		//(large_group.contains(mNodeA_idx) && large_group.contains(mNodeB_idx)) && 
		if((group_idx_A != group_idx_B)) {
			// 대규모 그룹의 엣지 추가
			large_graph.get(mNodeA).add(new int[] {mNodeB, mTime});
			large_graph.get(mNodeB).add(new int[] {mNodeA, mTime});
		}else {
			// 소규모 그룹의 엣지 추가
			small_graph.get(group_idx_A).get(mNodeA_idx).add(new int[] {mNodeB_idx, mTime});
			small_graph.get(group_idx_A).get(mNodeB_idx).add(new int[] {mNodeA_idx, mTime});
			
			ArrayList<ArrayList<int[]>> now_graph = small_graph.get(group_idx_A);
			int[] dist_1 = dijkstra(1, now_graph, 31);
			int[] dist_2 = dijkstra(2, now_graph, 31);
			
			int node_1 = group_idx_A * 100 + 1;
			int node_2 = group_idx_A * 100 + 2;
			int node_3 = group_idx_A * 100 + 3;
			
			for(int i=0; i<large_graph.get(node_1).size();i++) {
				if(large_graph.get(node_1).get(i)[0] == node_2) {
					large_graph.get(node_1).get(i)[1] = dist_1[2];		
				}else if(large_graph.get(node_1).get(i)[0] == node_3) {
					large_graph.get(node_1).get(i)[1] = dist_1[3];		
				}
			}
			
			for(int i=0; i<large_graph.get(node_2).size();i++) {
				if(large_graph.get(node_2).get(i)[0] == node_1) {
					large_graph.get(node_2).get(i)[1] = dist_2[1];	
				}else if(large_graph.get(node_2).get(i)[0] == node_3) {
					large_graph.get(node_2).get(i)[1] = dist_2[3];	
				}
			}
			
			for(int i=0; i<large_graph.get(node_3).size();i++) {
				if(large_graph.get(node_3).get(i)[0] == node_2) {
					large_graph.get(node_3).get(i)[1] = dist_2[3];	
				}else if(large_graph.get(node_3).get(i)[0] == node_1) {
					large_graph.get(node_3).get(i)[1] = dist_1[3];
					
//					large_graph.get(node_3).add(new int[] {node_1, dist_1[3]});	
				}
			}
		}
    }

	public void removeLine(int mNodeA, int mNodeB)
	{
        // 최대 200 호출
        // 1. 소규모 그룹 수정
        	// 대표 노드까지의 엣지 수정
		// 2. 대규모 그룹의 엣지 수정
		
		int mNodeA_idx = mNodeA % 100;
		int mNodeB_idx = mNodeB % 100;
		
		int group_idx_A = mNodeA / 100;
		int group_idx_B = mNodeB / 100;
		
		//(large_group.contains(mNodeA_idx) && large_group.contains(mNodeB_idx)) && 
		if((group_idx_A != group_idx_B)) {
			// 대규모 그룹의 엣지 제거
			for(int i=0; i< large_graph.get(mNodeA).size();i++) {
				if(large_graph.get(mNodeA).get(i)[0] == mNodeB) {
					large_graph.get(mNodeA).remove(i);
					break;
				}
			}
			
			for(int i=0; i< large_graph.get(mNodeB).size();i++) {
				if(large_graph.get(mNodeB).get(i)[0] == mNodeA) {
					large_graph.get(mNodeB).remove(i);
					break;
				}
			}
		}else {
			// 소규모 그룹의 엣지 제거
			for(int i=0; i< small_graph.get(group_idx_A).get(mNodeA_idx).size();i++) {
				if(small_graph.get(group_idx_A).get(mNodeA_idx).get(i)[0] == mNodeB_idx) {
					small_graph.get(group_idx_A).get(mNodeA_idx).remove(i);
					break;
				}
			}
			
			for(int i=0; i< small_graph.get(group_idx_B).get(mNodeB_idx).size();i++) {
				if(small_graph.get(group_idx_B).get(mNodeB_idx).get(i)[0] == mNodeA_idx) {
					small_graph.get(group_idx_B).get(mNodeB_idx).remove(i);
					break;
				}
			}

			// update;
			ArrayList<ArrayList<int[]>> now_graph = small_graph.get(group_idx_A);
			int[] dist_1 = dijkstra(1, now_graph, 31);
			int[] dist_2 = dijkstra(2, now_graph, 31);
			
			int node_1 = group_idx_A * 100 + 1;
			int node_2 = group_idx_A * 100 + 2;
			int node_3 = group_idx_A * 100 + 3;
			
			// 이거 때문에 overflow문제가 생긴거임;;;;;
			// 여기서 update하는 dist가 maxsize일 수 있었다.
			for(int i=0; i<large_graph.get(node_1).size();i++) {
				if(large_graph.get(node_1).get(i)[0] == node_2) {
					large_graph.get(node_1).get(i)[1] = dist_1[2];
				}else if(large_graph.get(node_1).get(i)[0] == node_3) {
					large_graph.get(node_1).get(i)[1] = dist_1[3];
				}
			}
			
			for(int i=0; i<large_graph.get(node_2).size();i++) {
				if(large_graph.get(node_2).get(i)[0] == node_1) {
					large_graph.get(node_2).get(i)[1] = dist_2[1];
				}else if(large_graph.get(node_2).get(i)[0] == node_3) {
					large_graph.get(node_2).get(i)[1] = dist_2[3];
				}
			}
			
			for(int i=0; i<large_graph.get(node_3).size();i++) {
				if(large_graph.get(node_3).get(i)[0] == node_2) {
					large_graph.get(node_3).get(i)[1] = dist_2[3];
				}else if(large_graph.get(node_3).get(i)[0] == node_1) {
					large_graph.get(node_3).get(i)[1] = dist_1[3];
				}
			}
		}
	}

	public int checkTime(int mNodeA, int mNodeB)
	{
        // 최대 700 호출
        // 루트노드끼리 최단 시간 확인하기
        // 10^5 이내로 끊어야 할듯
        
        // 다 여기서 계산하면 되긴할텐데 시간복잡도 아슬아슬.
        
        // union find 같은걸로 그룹핑 후
        // 그룹핑된 내부 시간을 다른데서 미리 계산해두기
		// 큰 그룹 다익스트라로 확인하기
		int dist[] = dijkstra(mNodeA, large_graph, (NN*100 + 31));
		return dist[mNodeB];
	}
}