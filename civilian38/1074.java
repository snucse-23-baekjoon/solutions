import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main{
    public static boolean between(int a, int x, int b){
        return (a <= x && x <= b);
    }
    public static int rcz(int target_row, int target_col, int min_row, int min_col, int max_row, int max_col, int min_val, int max_val){
        if(min_val == max_val){
            return min_val;
        } else {
            int col_mid_val = (max_col + min_col)/2;
            int row_mid_val = (max_row + min_row)/2;
            int unit = (max_val - min_val + 1) / 4;

            if(between(min_row, target_row, row_mid_val)){
                if(between(min_col, target_col, col_mid_val)){
                    return rcz(target_row, target_col, min_row, min_col, row_mid_val, col_mid_val, min_val, min_val + unit);
                } else {
                    return rcz(target_row, target_col, min_row, col_mid_val + 1, row_mid_val, max_col, min_val + unit, min_val + 2 * unit);
                }
            } else {
                if(between(min_col, target_col, col_mid_val)){
                    return rcz(target_row, target_col, row_mid_val + 1, min_col, max_row, col_mid_val, min_val + 2 * unit, min_val + 3 * unit);
                } else {
                    return rcz(target_row, target_col, row_mid_val + 1, col_mid_val + 1, max_row, max_col, min_val + 3 * unit, min_val + 4 * unit);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int row = Integer.parseInt(st.nextToken());
        int col = Integer.parseInt(st.nextToken());

        int answer = rcz(row, col, 0, 0, (int)Math.pow(2, n) - 1, (int)Math.pow(2, n) - 1, 0, (int)Math.pow(2, 2 * n) - 1);
        bw.write(answer + "\n");

        bw.flush();
        br.close();
        bw.close();
    }
}