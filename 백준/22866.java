import java.io.*;
import java.util.*;
// 건물이 총 N개 존재
// 각 건물 옥상에서 양 옆에 존재하는 건물의 옆을 몇 개 볼 수 있을지?

// 현재 있는 건물의 높이가 L이라고 가정하면 높이가 L보다 큰 곳의 건물만 볼 수 있음.
// 바라보는 방향으로 높이가 L인 건물 뒤에 높이가 L이하인 건물이 있다면 가려져서 안보임.
// 각 건물에서 볼 수 있는 건물들이 어떤 것이 있을까?

// 출력
// i번째 건물에서 볼 수 있는 건물의 개수
// 1개 이상이라면 건물에서 가장 가까운 건물의 번호 중 작은 번호로 출력

// N <= 100,000(10^5)
// O(NlogN)안으로 끊어야함.

// 3 7 1 6 3 5 1 7
// 점점 커지는 방향으로 자기자신보다 큰 수 찾기

// dp, 투 포인터, 탐색, 


public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        Deque<int[]> queue = new ArrayDeque<>();
        
        for(int i=0; i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        ArrayList<int[]> answer = new ArrayList<>();
        for(int i=0; i<N; i++){
            answer.add(new int[] {0,-1});
        }
        
        queue.offerFirst(new int[]{0,arr[0]});
        for(int i=1; i<N; i++){
            while(!queue.isEmpty()){
                int[] peek = queue.peekFirst();
                if(peek[1] <= arr[i]){
                    queue.pollFirst();
                }else{
                    break;
                }
            }
            
            if(!queue.isEmpty()){
                int[] peek = queue.peekFirst();
                answer.get(i)[0] += queue.size();
                answer.get(i)[1] = peek[0];
            }
            queue.offerFirst(new int[]{i,arr[i]});
        }
        queue.clear();
        queue.offerFirst(new int[]{N-1,arr[N-1]});
        for(int i = N-2; i>-1; i--){
            while(!queue.isEmpty()){
                int[] peek = queue.peekFirst();
                if(peek[1] <= arr[i]){
                    queue.pollFirst();
                }else{
                    break;
                }
            }
            
            if(!queue.isEmpty()){
                int[] peek = queue.peekFirst();
                answer.get(i)[0] += queue.size();
                int now_answer = answer.get(i)[1];

                if(answer.get(i)[1] == -1){
                    answer.get(i)[1] = peek[0];
                }else{
                    if(Math.abs(peek[0]-i) == Math.abs(now_answer-i)){
                        answer.get(i)[1] = (peek[0] < now_answer)? peek[0] : now_answer;
                    }else if(Math.abs(peek[0]-i) < Math.abs(now_answer-i)){
                        answer.get(i)[1] = peek[0];
                    }   

                }
            }
            queue.offerFirst(new int[]{i,arr[i]});
        }
        
        for(int i=0; i<N; i++){
            sb.append(answer.get(i)[0]).append(" ");
            if(answer.get(i)[0] == 0){
                sb.append("\n");
            }else{
                sb.append(answer.get(i)[1]+1).append("\n");
            }
        }
        System.out.print(sb);
    }

}