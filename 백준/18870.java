package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * 좌표 압축
 * 자기보다 작은 애들 갯수가 들어가게됨 
 * 1. 정렬 + Map만들기
 * 2. TreeMap으로 만들기
 * 
 * 여러 방법들
 * 1. 정렬 -> Map
 * 2. TreeMap
 * 3. Node
 * 
 */
public class BJ_18870 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		HashMap<Integer, Integer> hm = new HashMap<>();
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] org_arr = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			org_arr[i] = arr[i];
		}
		
		Arrays.sort(arr);
		int index = 0;
		for(int number : arr) {
			if(hm.containsKey(number)) {
				continue;
			}else {
				hm.put(number, index++);
			}
		}
		
		for(int i=0; i<N; i++) {
			sb.append(hm.get(org_arr[i])).append(" ");
		}
		System.out.print(sb);
	}

}
