import java.util.*;

public class Main {

    public static void main(String[] args)  {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int X = scan.nextInt();
        int K = scan.nextInt();

        for ( int i = 0; i < K; i++) {
            int A = scan.nextInt();
            int B = scan.nextInt();
            if ( A == X) {
                X = B;
            }
            else if ( B == X){
                X = A;
            }
        }
        System.out.println(X);
     }
}
