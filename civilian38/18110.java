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

        int repeat = Integer.parseInt(br.readLine());
        int[] score= new int[31];
        for (int i = 0; i < 31; i++){
            score[i] = 0;
        }

        for(int i = 0; i < repeat; i++){
            score[Integer.parseInt(br.readLine())]++;
        }



        // 하위 15% 삭제
        int cut = (int) Math.round((double)repeat * 0.15);
        int index = 0;
        while (cut > 0){
            score[index] -= cut;
            cut = - score[index];
            if(score[index] < 0){
                score[index] = 0;
            }
            index++;
        }

        // 상위 15% 삭제
        cut = (int) Math.round((double)repeat * 0.15);
        index = 30;
        while (cut > 0){
            score[index] -= cut;
            cut = - score[index];
            if(score[index] < 0){
                score[index] = 0;
            }
            index--;
        }

        int sum = 0;
        for(int i = 0; i < 31; i++){
            sum += i * score[i];
        }
        bw.write(String.valueOf(Math.round(((double)sum/(repeat - 2 * (int) Math.round((double)repeat * 0.15) ))) + "\n"));

        bw.flush();
        br.close();
        bw.close();
    }
}