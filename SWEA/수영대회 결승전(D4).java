/* 가장 빠른 경로로 갈 때 몇초 골인? */
/* 장애물 : 1 - 못지나감 */
/* 소용돌이 : 2초 유지되다가 1초 잠잠해짐 */
/* N <= 15 */

import java.io.*;
import java.util.*;

/*
   나는 일단 다익스트라로 풀었다. 장애물이 주기적으로 사라졌다가 나타나기 때문에 얼마나 기다려야 하는지
   측정할 수 있고, 이를 반영한 COST를 넘겨주도록 하여 계산하였다.
 */

class Node implements Comparable<Node>{
    int x, y, time;
    Node(int x, int y, int time){
        this.x = x;
        this.y = y;
        this.time = time;
    }
    @Override
    public int compareTo(Node other){
        return this.time - other.time;
    }
}

class Solution
{
    public static boolean inRange(int N, int i, int j){
        return i>=0 && i<N && j>=0 && j<N;
    }

	public static void main(String args[]) throws Exception
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T;
		T=Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = Integer.parseInt(br.readLine());
            int[][] arr = new int[N][N];
            /*상 하 좌 우 */
            int[] di = {-1,1,0,0};
            int[] dj = {0,0,-1,1};

            for(int i = 0; i < N; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int j =0; j<N;j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int start_i = Integer.parseInt(st1.nextToken());
            int start_j = Integer.parseInt(st1.nextToken());

            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int end_i = Integer.parseInt(st2.nextToken());
            int end_j = Integer.parseInt(st2.nextToken());

            int [][] time_arr = new int[N][N];
            for(int i = 0; i<N; i++){
                for(int j = 0; j<N; j++){
                    time_arr[i][j] = Integer.MAX_VALUE;
                }
            }

            PriorityQueue<Node> pq = new PriorityQueue<>();
            pq.offer(new Node(start_i, start_j, 0));
            time_arr[start_i][start_j] = 0;

            while(!pq.isEmpty()){
                Node now_node = pq.poll();
                int now_i = now_node.x;
                int now_j = now_node.y;
                int cost = now_node.time;

                if (now_i == end_i && now_j == end_j){
                    break;
                }

                if (time_arr[now_i][now_j] < cost){
                    continue;
                } 
                
                for(int k=0; k<4; k++){
                    int next_i = now_i + di[k];
                    int next_j = now_j + dj[k];

                    if(inRange(N, next_i, next_j)){
                        if(arr[next_i][next_j] == 0){
                            int new_cost = cost + 1;
                            if(time_arr[next_i][next_j] > new_cost){
                                pq.offer(new Node(next_i, next_j, new_cost));
                                time_arr[next_i][next_j] = new_cost;
                            }
                        }else if(arr[next_i][next_j] == 1){
                            continue;
                        }else if(arr[next_i][next_j] == 2){
                            if (cost % 3 == 2){
                                int new_cost = cost + 1;
                                if(time_arr[next_i][next_j] > new_cost){
                                    pq.offer(new Node(next_i, next_j, new_cost));
                                    time_arr[next_i][next_j] = new_cost;
                                }
                            }else if  (cost % 3 == 1){
                                int new_cost = cost + 2;
                                if(time_arr[next_i][next_j] > new_cost){
                                    pq.offer(new Node(next_i, next_j, new_cost));
                                    time_arr[next_i][next_j] = new_cost;
                                }
                            }else if  (cost % 3 == 0){
                                int new_cost = cost + 3;
                                if(time_arr[next_i][next_j] > new_cost){
                                    pq.offer(new Node(next_i, next_j, new_cost));
                                    time_arr[next_i][next_j] = new_cost;
                                }
                            }
                            
                        }
                    }

                }

            }
            /*-1처리해주기 */
            if (time_arr[end_i][end_j] == Integer.MAX_VALUE){
                System.out.println("#"+test_case+" "+-1);
            }else{
                System.out.println("#"+test_case+" "+time_arr[end_i][end_j]);
            }
            
		}
	}
}

/* 다익스트라 */