import java.io.*;
import java.util.*;
/*
 * 장난감 조립
 * 
 * 장난감을 만드는데 기본 부품과 그 기본 부품으로 조힙하여 만든 중간 부품이 사용된다. 
 * 기본부품
 * - 더 이상 분해 불가
 * 
 * 중간부품
 * - 또 다른 중간 부품이나, 기본부품을 이용하여 만들어지는 부품
 * 
 * 어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어졌을 때 하나의 완제품을 조립하기 위하여 필요한 기본 부품의 종류별 개수를 계산
 * 
 * N <= 100, M<=100
 * 
 * 이 문제는 근데 그냥 완성품을 시작점으로 해서 위상정렬 하면 쉽다.
 * 그래도 DP연습하려고 DP로 하기.
 * 
 * 그냥 그래프 완탐으로도 풀릴거 같은데? 
 * - 시간 초과 문제가 있다.
 * 
 * 1. 완탐할때(현재 인덱스, 필요 개수)
 *   값 : 사용 개수
 *   
 *   사용개수 return 받으면 count 곱해줘야 함. 
 * 
 *   그 안에서는 현재 인덱스와 연결된 다른 인덱스 찾아서 다시 재귀호출
 * 
 * Top down 방식의 DP로 풀었다.
 * 
 * Bottom up으로도 가능한가??
 * DP[i][j] : i부품을 만드는데 필요한 j부품의 수로 가능하다고 한다. (j는 기본 부품)
 * 
 */

public class BJ_2637 {
     static ArrayList<ArrayList<int[]>> graph;
     static TreeSet<Integer> basic;
     static ArrayList<HashMap<Integer, Integer>> map;

     static public void backtracking(int now_node){
          // if(basic.contains(now_node)){
          //      count_arr[now_node] += need;
          //      return;
          // }
          if(map.get(now_node).isEmpty()){
               for(int i : basic){
                    map.get(now_node).put(i, 0);
               }
          }

          for(int[] n : graph.get(now_node)){
               // 다음노드들 정보 

               int next_node = n[0];
               int ne = n[1];
               if(map.get(next_node).isEmpty()){
                    // 처음
                    backtracking(next_node);
               }
               // 이미 메모지에이션 적용 있음
               for(int key : map.get(next_node).keySet()){
                    map.get(now_node).put(key, map.get(now_node).get(key) + map.get(next_node).get(key) * ne);          
               }
          }
     }

     public static void main(String[] args) throws IOException{
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          StringTokenizer st;
          graph = new ArrayList<>();
          map = new ArrayList<>();

          int N = Integer.parseInt(br.readLine());
          int M = Integer.parseInt(br.readLine());
          for(int i=0; i<N+1;i++){
               graph.add(new ArrayList<>());
               map.add(new HashMap<>());
          }
          for(int i=0; i<M; i++){
          // 완제품 X를 만드는데 중간부품, 기본부품 Y가 K개 필요하다. 싸이클은 없다.
               st = new StringTokenizer(br.readLine());
               int X = Integer.parseInt(st.nextToken());
               int Y = Integer.parseInt(st.nextToken());
               int K = Integer.parseInt(st.nextToken());

               graph.get(X).add(new int[]{Y,K});
          }
          basic = new TreeSet<>();
          // 기본 부품 찾기
          for(int i=1; i<N+1; i++){
               if(graph.get(i).size() == 0){
                    basic.add(i);
               }
          }
          for(int b : basic){
               map.get(b).put(b, 1);
          }

          backtracking(N);
          for(int i : basic){
               System.out.println(i + " "+map.get(N).get(i));
          }

     }
}
