import java.io.*;
import java.util.*;

/*
 * 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇명이 있는지 구하는 프로그램
 * 친구 네트워크란 친구 관계만으로 이동할 수 있는 사이
 * 
 * 테스트 케이스 개수
 * 친구 관계의 수 F <= 100,000
 */

public class BJ_4195 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static HashMap<Integer, Integer> parents;
    static HashMap<Integer, Integer> counts;

    public static void union(int a, int b){
        a = find_parents(a);
        b = find_parents(b);

        if(a < b){
            parents.put(b, a);
            counts.put(a, counts.get(a) + counts.get(b));
        }else if(a > b){
            parents.put(a, b);
            counts.put(b, counts.get(a) + counts.get(b));
        }
    }

    public static int find_parents(int a){
        if(a != parents.get(a)){
            parents.put(a, find_parents(parents.get(a)));
        }
        return parents.get(a);
    }

    public static void main(String[] args) throws IOException{
        int T = Integer.parseInt(br.readLine());
        for(int i=0; i<T; i++){
            HashMap<String,Integer> s_to_idx = new HashMap<>();
            parents = new HashMap<>();
            counts = new HashMap<>();

            int K = Integer.parseInt(br.readLine());
            int index = 0;
            for(int k=0; k<K; k++){
                st = new StringTokenizer(br.readLine());
                String str1 = st.nextToken();
        
                if(!s_to_idx.containsKey(str1)){
                    s_to_idx.put(str1, index);
                    parents.put(index, index);
                    counts.put(index, 1);
                    index++;
                }

                String str2 = st.nextToken();
                if(!s_to_idx.containsKey(str2)){
                    s_to_idx.put(str2, index);
                    parents.put(index, index);
                    counts.put(index, 1);
                    index++;
                }

                int n1 = s_to_idx.get(str1);
                int n2 = s_to_idx.get(str2);

                union(n1, n2);
                sb.append(counts.get(find_parents(n1))).append('\n');
            }
            // System.out.println(parents.toString());
        }
        System.out.println(sb);
    }
}
