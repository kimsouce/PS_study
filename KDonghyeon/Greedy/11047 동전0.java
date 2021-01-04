package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("동전 종류의 개수와 원하는 가치의 합을 입력하시오.");
        int n = scan.nextInt();
        int m = scan.nextInt();
        int []coin = new int[n];
        int count = 0;

        for ( int i = 0; i < n; i++) {
            coin[i] = scan.nextInt();
        }
        count = takeCount(coin, count, n, m);
        System.out.println(count);
    }

    static int takeCount(int[]coin, int count, int n, int m ) {
        for ( int i = n-1; i >=0; i--) {
            if ( m == 0 ) {
                break;
            }
            if ( coin[i] > m ) {
                continue;
            }
            else {
                count += m / coin[i];
                m = m % coin[i];
            }
        }
        return count;
    }

}
