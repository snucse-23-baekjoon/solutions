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
        int[][] house = new int[15][14];
        for(int j = 0; j < 14; j++){ house[0][j] = j + 1; }
        for(int j = 0; j < 15; j++){ house[j][0] = 1; }
        for(int i = 1; i < 15; i++){
            for(int j = 1; j < 14; j++){
                house[i][j] = house[i-1][j] + house[i][j - 1];
            }
        }

        for(int i = 0; i < n; i++){
            int floor = Integer.parseInt(br.readLine());
            int room = Integer.parseInt(br.readLine());

            bw.write(String.valueOf(house[floor][room - 1]));
            bw.newLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}