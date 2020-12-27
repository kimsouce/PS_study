package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println(" 로프의 개수 및 각 로프 별 최대 중량에 대해 입력하시오 :  ");
        int n = scan.nextInt();
        int result = 0;
        Integer[] weigh = new Integer[n];
        for(int i = 0; i < n; i++)
            weigh[i] = scan.nextInt();
        Arrays.sort(weigh, Collections.reverseOrder());
        // 내림차순으로 정리 해야 하는 이유
        // 1. 임의로 선택한 K에 있는 무게 중에서, 최소 값의 무게가 견딜 수 있는 최대 하중에 따라
        // 2. 다른 로프들이 견딜 수 있는 무게가 결정 되기 때문에
        // 3. 내림차순으로 정렬 할 경우, 자기자신이 K라는 임의의 리스트에서 최소값이 되어 k의 길이 만큼 곱했을 때
        // 4. K 개의 로프가 버틸 수 있는 최대 하중이 계산 될 수 있다.

        for(int k = 1; k <= n; k++)
            result = Math.max(result, weigh[k-1]*k);
        System.out.println(result);
    }
}
