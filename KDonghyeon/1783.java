package com.company;
import java.util.Scanner;

public class Main {

    static int n,m;
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        n = sc.nextInt();
        m = sc.nextInt();

        System.out.println(solve());

    }

    static int solve() {
        if ( n == 1) {
            return 1;
        }
        else if (n == 2) {
            return Math.min(4, (m+1)/2);
        }

        else {
            if ( m < 7) {
                return Math.min(4, m);
            }
            else if ( m == 5) {
                return 5;
            }
            else
                return m-2;
        }

    }
}

