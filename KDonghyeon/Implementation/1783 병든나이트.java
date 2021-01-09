package com.company;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n,m;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        System.out.println(solve(n,m));

    }

    static int solve(int n, int m) {
        if ( n == 1) { // 이동이 불가능 => 1로 리턴한다.
            return 1;
        }
        else if (n == 2) { // 높이가 2일때는, 2칸 위로 작동이 불가능하다.
            // 그리하여 길이가 길어진다고 해도, 4회보다 이동이 적을 때만 규칙과 상관 없는 이동이 가능하기에
            // 4와 이동 가능 횟수를 비교하여 최소 값을 반환해준다.
            return Math.min(4, (m+1)/2);
        }

        else {
            if ( m < 7)  {
                // n ==2 일 떄와 마찬기지로,
                return Math.min(4, m);
            }
            else
                return m-2;
        }

    }
}
