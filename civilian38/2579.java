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
        int[][] stairs = new int [number + 1][2];
        int[] scores = new int[number + 1];
        for(int i = number - 1; i >= 0; i--){
            scores[i] = Integer.parseInt(br.readLine());
        }
        scores[number] = 0;
        for(int i = 0; i < number + 1; i++){
            if(i == 0){
                stairs[i][0] = scores[i];
                stairs[i][1] = scores[i];
                if(i == number){
                    bw.write(String.valueOf(scores[i]));
                }
            } else if(i == 1){
                stairs[i][0] = scores[i] + stairs[i - 1][1];
                if(i == number){
                    bw.write(String.valueOf(stairs[i][0]));
                }
            } else if(i == 2){
                stairs[i][1] = scores[i] + stairs[i - 2][0];
                if(i == number){
                    bw.write(String.valueOf(Math.max(stairs[i][1], stairs[i - 1][0])));
                }
            } else {
                stairs[i][0] = scores[i] + stairs[i - 1][1];
                stairs[i][1] = Math.max(scores[i] + stairs[i - 2][0], scores[i] + stairs[i - 2][1]);
                if(i == number){
                    bw.write(String.valueOf(Math.max(stairs[i - 1][0], Math.max(stairs[i][0], stairs[i][1]))));
                }
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}