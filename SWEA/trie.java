
import java.util.*;

/*
 * 문자열을 저장하고, 빠르게 탐색하기 위한 트리 형태 자료구조
 * 문자열 저장을 위해 메모리를 사용하는 대신, 탐색속도 매우 빠름 O(K)
 * 
 * 문자열의 각 문자를 트리 노드로 표현하여, 같은 접두사를 가진 문자열들이 트리에서
 * 같은 경로를 공유하도록 만든 자료구조.
 * 
 * 이 접두사로 시작하는 모든 데이터를 찾아줘라는 요구사항에서 사용될 수 있음
 * 
 * 규칙 
 * - 루트 노드는 비어있다. 
 * - 루트 노드의 자식노드는 각 단어들의 첫 글자이다.
 * - 색 칠해져 있는 노드는 각 문자열의 마지막 글자이다.
 * 
 * 각 노드의 자식노드들을 Map에 저장한다.
 * 해당 노드가 마지막을 뜻하는 endofword를 저장할 boolean 필드를 갖는다.
 * 
 * 1. insert
 * 2. search
 * 3. startWith
 *  - 접두사 탐색
 * 4. delete
 */

 /*
  * 자식 개수가 하나일 때 자동완성
  * 사전에 있는 단어들을 입력하기 위해 버튼을 눌러야 하는 횟수의 평균 구하기
  */
public class trie {
    static public class Node {
        HashMap<Character,Node> children = new HashMap<>();
        boolean isEnd = false;
    }
    static Node root;

    static public void insert(String str){
        Node nowNode = root;
        for(int i = 0; i<str.length();i++){
            char c = str.charAt(i);
            if(!nowNode.children.containsKey(c)){
                nowNode.children.put(c, new Node());
            }
            nowNode = nowNode.children.get(c);
        }
        nowNode.isEnd = true;
    }

    static public boolean search(String str){
        boolean find = false;
        Node nowNode = root;
        for(int i=0;i<str.length();i++){
            char c = str.charAt(i);
            if(nowNode.children.containsKey(c)){
               nowNode = nowNode.children.get(c); 
            }else{
                return false;
            }
        }
        if(nowNode.isEnd){
            find = true;
        }
        return find;
    }

    static public boolean delete(String str){
        return delete(root, str, 0);
    }

    static public boolean delete(Node node, String str, int index){
        char ch = str.charAt(index);
        index++;
        Node childNode = node.children.get(ch);
        if(index == str.length()){
            if(!childNode.isEnd){
                return false;
            }
            childNode.isEnd = false;
            if(childNode.children.isEmpty()){
                node.children.remove(ch);
            }
        }else{
            if(delete(childNode, str, index)){
                if(!childNode.isEnd && childNode.children.isEmpty()){
                    node.children.remove(ch);
                }
            }else{
                return false;
            }
        }
        return true;
    }
}

