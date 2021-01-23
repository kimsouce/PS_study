package com.company;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static class Po {
        char ch;
        int num;
        public Po(char ch, int n) {
            this.ch = ch;
            this.num = n;
        }
    }

    static String str1,str2;
    static ArrayList<Po> arrayList = new ArrayList<Po>(); // 배열과 같지만, 크기가 자동으로 증가한다.
    // 타입설정 PO 객체만 사용이 가능하다.
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N1, N2;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N1 = Integer.parseInt(st.nextToken());
        N2 = Integer.parseInt(st.nextToken());
        // 각 개미의 집단의 수를 입력받는다.

        str1 = br.readLine();
        for ( int i = str1.length()-1; i >= 0; i--) {
            arrayList.add(new Po(str1.charAt(i),1));
        } // 1번 집단을 -> 방향으로 보이게 하기 위해서 역으로 list에 저장한다.

        str2 = br.readLine();
        for ( int i =0; i < str2.length(); i++) {
            arrayList.add(new Po(str2.charAt(i), 2));
        }// 2번 집단을 <- 방향으로 담는건 정방향이기에, 그대로 list에 저장한다.

        int test_case = Integer.parseInt(br.readLine()); // test의 수를 입력받는다.

        while (test_case -- > 0) {
            for ( int i = 0; i < arrayList.size()-1; i++) {
                Po current = arrayList.get(i);
                Po next = arrayList.get(i+1);
                if(current.num != 2 && current.num != next.num) {
                    arrayList.set(i,next);
                    arrayList.set(i+1, current);
                    i++;
                }
            }

        }
        for (int i =0; i< arrayList.size(); i++) {
            System.out.print(arrayList.get(i).ch);
        }

    }
}
