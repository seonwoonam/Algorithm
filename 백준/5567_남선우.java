import java.io.*;
import java.util.*;

// 자신의 친구와 친구의 친구까지만 초대
// 상근이의 동기 N명(1번 ~ N번)
// 상근이 학번은 1번

// 상근이 동기들의 친구관계를 모두 조사한 리스트

// 출력 
// 결혼식에 초대할 사람의 수

// N<=500
// M<=10000

// bfs 통해서 상근이 친구 찾고, 뎁스가 1명 더 들어갈 때 까지만 초대하는 방식으로 구현 
class Main{
    public static void main(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(N+1);
        for(int i=0; i<=N;i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            int first = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            graph.get(first).add(end);
            graph.get(end).add(first);
        }
        
        boolean[] visited = new boolean[N+1];
        Deque<int[]> que = new ArrayDeque<>();
        
        que.offerLast(new int[]{1, 0});
        visited[1] = true;
        int result = -1;
        
        while(!que.isEmpty()){
            int[] now_data = que.pollFirst();
            if(now_data[1] > 2){
                continue;
            }
            result += 1;
            for(int i=0; i<graph.get(now_data[0]).size();i++){
                int next_node = graph.get(now_data[0]).get(i);
                if(!visited[next_node]){
                    que.offerLast(new int[]{next_node, now_data[1]+1});
                    visited[next_node] = true;
                }
            }
        }
        System.out.println(result);
        
    }
}