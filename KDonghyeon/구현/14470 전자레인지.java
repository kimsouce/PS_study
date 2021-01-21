import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        int D = Integer.parseInt(br.readLine());
        int E = Integer.parseInt(br.readLine());
        int time = 0;

        if ( A <= 0 ) {
            int temp = -(A);
            time += (B*E) + (temp*C) + D;
        }
        else if ( A > 0 ) {
            B -= A;
            time = B*E;
        }
        System.out.println(time);
    }
}
