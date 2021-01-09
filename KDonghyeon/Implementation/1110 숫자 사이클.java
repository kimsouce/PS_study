package com.company;
import java.io.BufferedReader; 
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = N;
        int count = 0;

        while ( true ) {
            N = ( (N%10)*10 ) + ( ((N/10) + (N%10))%10 );
            count++;
            if ( N == result) {
                break;
            }
        }
        System.out.println(count);
    }
}
