package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("대기 인원 및 인당 소요시간을 입력하시오 : ");
        int n = scan.nextInt();
        int[] time = new int [n];
        int prev = 0;
        int result = 0;

        for ( int i = 0; i < n; i++) {
            time[i] = scan.nextInt();
        }
        Arrays.sort(time); // 최소 대기시간을 구하려면, 오름차순 배열로 정리가 필요하다.
        result = calMinimum(n,prev,result,time);
        System.out.println(result);
    }

    static int calMinimum( int n, int prev, int result, int [] time) {
        for(int i = 0; i < n; i++) {
            result += prev + time[i]; // 자신의 값과 이전의 모든 값들을 더한 prev 변수와 더해준다.
            prev += time[i]; // i 이전의 모든 값들을 저장한다.
        }
        return result; // 결과를 반환한다.
    }
}
