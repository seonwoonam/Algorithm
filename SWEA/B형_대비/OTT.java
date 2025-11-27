import java.util.Scanner;

class Solution
{   
    private static UserSolution usersolution = new UserSolution();

    private final static int CMD_INIT       = 100;
    private final static int CMD_ADD        = 200;
    private final static int CMD_ERASE      = 300;
    private final static int CMD_WATCH      = 400;
    private final static int CMD_SUGGEST    = 500;
    
    public final static class RESULT
    {
        int cnt;
        int[] IDs = new int[5];
        
        RESULT()
        {
            cnt = -1;
        }
    }
    
    private static boolean run(Scanner sc) throws Exception
    {
        int Q, N;
        int mID, mGenre, mTotal, mRating, uID;
        
        int ret = -1, cnt, ans;

        RESULT res;

        Q = sc.nextInt();

        boolean okay = false;

        for (int q = 0; q < Q; ++q)
        {
            int cmd;
            cmd = sc.nextInt();

            switch(cmd)
            {
            case CMD_INIT:
                N = sc.nextInt();
                usersolution.init(N);
                okay = true;
                break;
            case CMD_ADD:
                mID = sc.nextInt();
                mGenre = sc.nextInt();
                mTotal = sc.nextInt();
                ret = usersolution.add(mID, mGenre, mTotal);
                ans = sc.nextInt();
                if (ret != ans)
                    okay = false;
                break;
            case CMD_ERASE:
                mID = sc.nextInt();
                ret = usersolution.erase(mID);
                ans = sc.nextInt();
                if (ret != ans)
                    okay = false;
                break;
            case CMD_WATCH:
                uID = sc.nextInt();
                mID = sc.nextInt();
                mRating = sc.nextInt();
                ret = usersolution.watch(uID, mID, mRating);
                ans = sc.nextInt();
                if (ret != ans)
                    okay = false;
                break;
            case CMD_SUGGEST:
                uID = sc.nextInt();
                res = usersolution.suggest(uID);
                cnt = sc.nextInt();
                if (res.cnt != cnt)
                    okay = false;
                for (int i = 0; i < cnt; ++i)
                {
                    ans = sc.nextInt();
                    if (res.IDs[i] != ans)
                        okay = false;
                }
                break;
            default:
                okay = false;
                break;
            }
        }

        return okay;
    }

    public static void main(String[] args) throws Exception
    {
        //System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

        Scanner sc = new Scanner(System.in);
        
        int TC = sc.nextInt();
        int MARK = sc.nextInt();
        
        for (int testcase = 1; testcase <= TC; ++testcase)
        {
            int score = run(sc) ? MARK : 0;
            System.out.println("#" + testcase + " " + score);
        }

        sc.close();
    }
}

class UserSolution
{
    void init(int N)
    {
        return;
    }
    
    int add(int mID, int mGenre, int mTotal)
    {
        return -1;
    }
    
    int erase(int mID)
    {
        return -1;
    }

    int watch(int uID, int mID, int mRating)
    {
        return -1;
    }
    
    Solution.RESULT suggest(int uID)
    {
        Solution.RESULT res = new Solution.RESULT();
        
        res.cnt = -1;
        
        return res;
    }
}