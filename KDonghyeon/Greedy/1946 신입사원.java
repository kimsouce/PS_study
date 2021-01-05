import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case = Integer.parseInt(br.readLine());
        for(int i=0; i<test_case; i++) {
            int N = Integer.parseInt(br.readLine());
            int[][] apply = new int[N][2];	
            int count = 1;
            for(int j=0; j<N; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                apply[j][0] = Integer.parseInt(st.nextToken());
                apply[j][1] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(apply, new Comparator<int[]>() {
                @Override
                public int compare(int[] arr1, int[] arr2) {
                    return Integer.compare(arr1[0], arr2[0]);
                }
            });

            int standard = apply[0][1];	
            for(int j=1; j<N; j++) {
                if(apply[j][1] < standard) {	
                    standard = apply[j][1];	
                    count ++;
                }
            }
            System.out.println(count);
        }
    }
}
