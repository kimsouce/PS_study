package com.company;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine()); // 강의실 개수 입력
        int[] apply = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) { // 강의실 별 인원 수 입력
            apply[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken()); // 총 감독관 감시 가능 인원 수
        int c = Integer.parseInt(st.nextToken()); // 부 감독관 감시 가능 인원 수
        System.out.println(solution(apply, b, c));
    }

    private static long solution(int[] apply, int b, int c) {
        long count = 0;
        for (int i = 0; i < apply.length; i++) {
            apply[i] -= b; // 총 감독관 감시 인원 빼기 ( 1반에 1명의 총 감독관이 필요하기 때문 )
            count++;
            if (apply[i] > 0) {
                count += apply[i] / c; // ( 남은 인원을 부 감독관의 감시수로 빼고, 나머지가 0이상 이면 count를 1개 올려주면 => 최소 인원 구해진다 )
                if (apply[i] % c != 0)
                    count++;
            }
        }
        return count;
    }
}
