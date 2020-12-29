package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("요구되는 희의의 수와 시간을 모두 작성하시오 : ");
        int n = scan.nextInt();
        int [][]time = new int[n][2];
        int count = 0;

        for ( int i = 0; i < n; i++) {
            time[i][0] = scan.nextInt();
            time[i][1] = scan.nextInt();
        }

        count = counting(time, count, n);
        System.out.println(count);
    }

    static int counting(int[][]time, int count, int n ) {
        int prev_end = 0;
        Arrays.sort(time, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2 ) {
                // 종료 시간이 같다면, 시작 시간을 기준으로 정렬
                if (o1[1] == o2[1]) {
                    return o1[0] - o2[0];
                }
                // 다르다면, 시작 시간을 기준으로 정렬
                else
                    return o1[1] - o2[1];
            }
        });


        for ( int i = 0; i < n; i++) {
            if (prev_end <= time[i][0]) {
                prev_end = time[i][1];
                count++;
            }
        }
        return count;
    }
}
