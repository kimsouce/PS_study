package com.company;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case = Integer.parseInt(br.readLine());
        char [] first = new char[30];
        char [] second = new char[30];

        for ( int i = 0; i < test_case; i++) {
            String s = br.readLine();
            if ( s.length() % 2 == 0 ) {
                for ( int j = 0; j < s.length(); j++) {
                    if ( j % 2 == 0 ) {
                        first[j] = (s.charAt(j));
                    }
                    else {
                        second[j] = s.charAt(j);
                    }
                }
                System.out.println(first);
                System.out.println(second);
            } else {
                for ( int j = 0; j < s.length(); j++) {
                    if ( j % 2 == 0 ) {
                        first[j] = s.charAt(j);
                    }
                    else
                        second[j] = s.charAt(j);
                }
                char[] first_result = new char[first.length + second.length];
                System.arraycopy(first, 0, first_result, 0, first.length);
                System.arraycopy(second, 0, first_result, first.length, second.length);
                char [] second_result = new char[first.length + second.length];
                System.arraycopy(second, 0, second_result, 0, second.length);
                System.arraycopy(first, 0, second_result, second.length, first.length);
                System.out.println(first_result);
                System.out.println(second_result);


            }
        }
    }
}
