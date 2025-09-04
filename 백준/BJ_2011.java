import java.io.*;
/*
 * A는 1이라 하고, B는 2로, Z=26
 * 어떤 암호가 주어졌을 때, 그 암호에 대한 해석이 몇가지 나올 수 있는지 구한다.
 * 
 * 출력 : 1000000으로 나눈 나머지
 * 암호가 잘못되어 해석 못하면 0을 출력.
 * 
 * 1. 완탐으로 구현한다 했을 때 생각해보자
 *  - 최대 길이가 2개이다.
 *  
 *  - 1 문자열을 선택한 경우와
 *  - 2 문자열을 선택한 경우
 *  - backtracking(string str, string now_password)
 * 
 *  DP[현재_str] = 현재_str 일 때, 암호 해석에 대한 경우의 수.
 *  DP[현재_str] = DP[현재_Str-1] + DP[현재_str - 2]
 * 
 *  암호가 잘못 들어가는 경우 0이 이상한데 있을 때 
 * 
 * DP 자체를 생각하는거는 괜찮은데, 예외처리가 많아서 정답률이 낮은듯 하다.
 * - DP[i] 자체에 모듈러 연산을 넣어줘야한다.
 */ 

public class BJ_2011 {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int N = str.length();
        long[] dp = new long[N];


        if(str.charAt(0) == '0'){
            System.out.println(0);
            return;
        }

        if(N==1){
            System.out.println(1);
            return;
        }

        String temp = str.charAt(0)+ "" +str.charAt(1);


        for(int i=1; i<N; i++){
            if(str.charAt(i) == '0'){
                if(str.charAt(i-1) == '2' || str.charAt(i-1) == '1'){
                    continue;
                }
                System.out.println(0);
                return;
            }
        }

        if(Integer.parseInt(temp) > 26){
            dp[0] = 1;
            dp[1] = 1;
        }else if(Integer.parseInt(temp) == 20 || Integer.parseInt(temp) == 10){
            dp[0] = 1;
            dp[1] = 1;
        }
        else{
            dp[0] = 1;
            dp[1] = 2;
        }

        for(int i=2; i<N; i++){
            temp = str.charAt(i-1)+ "" +str.charAt(i);
            if(Integer.parseInt(temp) > 26){
                // 분해 안됨
                dp[i] = dp[i-1];
            }else if(str.charAt(i-1) == '0'){
                // 앞 자리가 0일 때 분해 안됨
                dp[i] = dp[i-1];
            }
            else if(Integer.parseInt(temp) == 20 || Integer.parseInt(temp) == 10){
                dp[i] = dp[i-2];
            }
            else{
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000;   
            }
        }
        System.out.println(dp[N-1]);
    }
}
