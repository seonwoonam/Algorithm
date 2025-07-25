import java.io.*;
import java.util.HashMap;
import java.util.HashSet;

/**
 * 색상 이름과 닉네임 순서로 이어서 팀명을 지으면 icpc 리저널에서 수상
 * Q개에 팀에 대해 다음 리저널에서 수상 가능할지
 * 
 * C, N
 * C개 줄에는 색상 이름 C개 제공
 * N개 줄에는 닉네임들 제공
 * Q개의 팀의 개수 제공
 * 팀명 제공
 * 
 * tries 사용
 * 색상의 끝에 end 표시
 * 닉네임 끝에 end 표시
 * 
 * 그냥 푼다면?
 * - 시간복잡도가 어떻게 될까?
 */
class Main {
    static class Node{
        HashMap<Character, Node> children = new HashMap<>();
        boolean isEnd = false;
    }

    static Node color_root;
    static Node nick_root;

    // 모두 넣기
    static void color_insert(String str){
        Node nowNode = color_root;
        for(int i=0;i<str.length();i++){
            char c = str.charAt(i);
            if(!nowNode.children.containsKey(c)){
                nowNode.children.put(c, new Node());
            }
            nowNode = nowNode.children.get(c);
        }

        nowNode.isEnd = true;
    }

    static void nickname_insert(String str){
        Node nowNode = nick_root;
        for(int i=str.length()-1;i>-1;i--){
            char c = str.charAt(i);
            if(!nowNode.children.containsKey(c)){
                nowNode.children.put(c, new Node());
            }
            nowNode = nowNode.children.get(c);
        }
        nowNode.isEnd = true;
    }

    // 서로 다른 자료구조 사용하기
    // 1. Color 자료구조
    // 2. NickName 자료구조

    // color는 앞으로, nickname은 뒤로 가는 방식으로 구현

    static String search(String str){
        Node color_node = color_root;
        Node nick_node = nick_root;
        HashSet<Integer> color_set = new HashSet<>();
        HashSet<Integer> nick_set = new HashSet<>();

        for(int i=0; i<str.length();i++){
            char c = str.charAt(i);
            if(!color_node.children.containsKey(c)){
                break;
            }
            color_node = color_node.children.get(c);
            if(color_node.isEnd){
                color_set.add(i);
            }
        }

        for(int i=str.length()-1;i>-1;i--){
            char c = str.charAt(i);
            if(!nick_node.children.containsKey(c)){
                break;
            }
            nick_node = nick_node.children.get(c);
            if(nick_node.isEnd){
                nick_set.add(i);
            }
        }

        for(Integer idx : color_set){
            if(nick_set.contains(idx+1)){
                return "Yes";
            }
        }

        return "No";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] first_input = br.readLine().split(" ");
        int C = Integer.parseInt(first_input[0]);
        int N = Integer.parseInt(first_input[1]);
        color_root = new Node();
        nick_root = new Node();

        for(int i=0; i<C; i++){
            String str_color = br.readLine().trim();
            color_insert(str_color);
        }

        for(int i=0; i<N; i++){
            String str_nickname = br.readLine().trim();
            nickname_insert(str_nickname);
        }

        int Q = Integer.parseInt(br.readLine());
        for(int i=0; i<Q; i++){
            String str_team = br.readLine().trim();
            sb.append(search(str_team)).append('\n');
        }
        System.out.println(sb);
    }
}


