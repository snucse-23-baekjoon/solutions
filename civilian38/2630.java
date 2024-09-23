import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main{
    public static int[] rcp(int[][] map, int min_row, int max_row, int min_col, int max_col){
        int sum = 0;
        for(int i = min_row; i <= max_row; i++){
            for(int j = min_col; j <= max_col; j++){
                sum += map[i][j];
            }
        }
        if(sum == 0){
            return new int[]{1, 0};
        } else if (sum == (int)Math.pow(max_row - min_row + 1, 2)){
            return new int[]{0, 1};
        } else {
            int mid_col = (max_col + min_col) / 2;
            int mid_row = (max_row + min_row) / 2;
            int[] minColSeries = new int[]{min_col, mid_col + 1, min_col, mid_col + 1};
            int[] maxColSeries = new int[]{mid_col, max_col, mid_col, max_col};
            int[] minRowSeries = new int[]{min_row, min_row, mid_row + 1, mid_row + 1};
            int[] maxRowSeries = new int[]{mid_row, mid_row, max_row, max_row};
            int[] tempAnswer = new int[]{0,0};

            for(int i = 0; i < 4; i++){
                int[] temp = rcp(map, minRowSeries[i], maxRowSeries[i], minColSeries[i], maxColSeries[i]);
                tempAnswer[0] += temp[0];
                tempAnswer[1] += temp[1];
            }

            return tempAnswer;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int size = Integer.parseInt(br.readLine());
        int[][] map = new int[size][size];
        for (int i = 0; i < size; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < size; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] answer = rcp(map, 0, size - 1, 0, size - 1);
        bw.write(answer[0] + "\n");
        bw.write(answer[1] + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}