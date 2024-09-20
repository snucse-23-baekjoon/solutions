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

        int number = 665;
        while(n > 0){
            number++;
            int copy = number;
            while(copy > 0){
                if(copy % 10 == 6 && (copy % 100) / 10 == 6 && (copy % 1000) / 100 == 6){
                    n--;
                    break;
                }
                copy /= 10;
            }
        }

        bw.write(String.valueOf(number));

        bw.flush();
        br.close();
        bw.close();
    }
}