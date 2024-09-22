import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int[] sizes = new int[6];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 6; i++) {
            sizes[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        int t = 0;
        int p1 = 0, p2 = 0; //p1: 묶음수 p2: 낱개수

        for (int i = 0; i < 6; i++){
            t += (sizes[i] % T > 0) ? sizes[i] / T + 1 : sizes[i] / T;
        }
        p1 = n / P;
        p2 = n - (P * p1);

        bw.write(String.valueOf(t));
        bw.newLine();
        bw.write(p1 + " " + p2);
        bw.flush();

        br.close();
        bw.close();
    }
}