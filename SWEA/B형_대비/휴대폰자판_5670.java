
import java.io.*;
import java.util.*;

// trie 예제
class Main_5670 {
    static class Node {
        HashMap<Character, Node> children = new HashMap<>();
        boolean isEnd = false;
    }
    static Node root;
    
    static void insert(String str){
        Node nowNode = root;
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(!nowNode.children.containsKey(c)){
                nowNode.children.put(c, new Node());
            }
            nowNode = nowNode.children.get(c);
        }
        nowNode.isEnd = true;
    }

    static int search_count(String str){
        // 자기 뒤에 여러 갈래가 있는지 확인함으로써 count ++ 해줌
        int count = 1;
        Node nowNode = root.children.get(str.charAt(0));
        for (int i = 1; i < str.length(); i++) {
            char c = str.charAt(i);
            if(nowNode.children.containsKey(c)){
                if(nowNode.children.size() > 1){
                    count += 1;
                }else if(nowNode.children.size() == 1 && nowNode.isEnd){
                    count += 1;
                }
                nowNode = nowNode.children.get(c);
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String T_str;
        while((T_str = br.readLine())!= null){
            int T = Integer.parseInt(T_str);
            String[] arr = new String[T];
            for(int i=0; i<T;i++){
                arr[i] = br.readLine();
            }

            root = new Node();
            for(String str : arr){
                insert(str);
            }
            int result = 0;
            for(String str : arr){
                result += search_count(str);
            }

            System.out.println(String.format("%.2f",((double)result/(double)T)));
     
        }
    }
}