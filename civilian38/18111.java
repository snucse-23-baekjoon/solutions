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

        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int[][] map = new int [m][n];

        int leastHeight = Integer.MAX_VALUE;
        int mostHeight = 0;
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] < leastHeight){
                    leastHeight = map[i][j];
                } else if(map[i][j] > mostHeight){
                    mostHeight = map[i][j];
                }
            }
        }

        int prev = Integer.MAX_VALUE;
        for(int height = mostHeight; height >= leastHeight; height--){
            int toBreak = 0;
            int toBuild = 0;
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    toBreak += (map[i][j] > height) ? map[i][j] - height : 0;
                    toBuild += (height > map[i][j]) ? height - map[i][j] : 0;
                }
            }

            if(toBreak + b >= toBuild){
                int time = 2 * toBreak + toBuild;
                if(time >= prev){
                    bw.write(String.valueOf(prev) + " " + String.valueOf(height + 1));
                    break;
                } else {
                    prev = time;
                    if(height == leastHeight){
                        bw.write(String.valueOf(prev) + " " + String.valueOf(height));
                    }
                }
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}