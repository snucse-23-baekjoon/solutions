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

        int number = Integer.parseInt(br.readLine());
        int[][] data = new int[number][2];

        for (int i = 0; i < number; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            data[i][0] = Integer.parseInt(st.nextToken());
            data[i][1] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < number; i++) {
            int front = 0;
            for(int j = 0; j < number; j++) {
                if(data[j][0] > data[i][0] && data[j][1] > data[i][1]){
                    front++;
                }
            }
            bw.write(String.valueOf(front + 1) + ' ');
        }
        bw.flush();
        br.close();
        bw.close();
    }
}