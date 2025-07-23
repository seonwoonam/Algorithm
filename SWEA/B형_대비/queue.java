import java.util.*;
public class queue {
    // 재귀 활용해서 삼각형 그리기
    static void printTriangle(int i){
        if(i==0){
            return; 
        }
        printTriangle(i-1);
        for(int j=0;j<i;j++){
            System.out.print("*");
        }
        System.out.println();
    }

    // 하노이 탑
    // static 
    
    public static void main(String args[]) throws Exception
	{
        // int N = 20;
        // int person = 1;
        // ArrayDeque<int[]> queue = new ArrayDeque<>();
        // queue.offer(new int[] {person, 1});
        // while(N>0){
        //     int[] cur = queue.poll();

        // }

        // 직각 삼각형 그리기
        printTriangle(4);
    }
}
