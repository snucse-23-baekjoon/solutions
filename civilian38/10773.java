import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int number = Integer.parseInt(br.readLine());
        ArrayList<Integer> money = new ArrayList<>();
        for (int i = 0; i < number; i++){
            int next = Integer.parseInt(br.readLine());
            if(next == 0){
                money.remove(money.size() - 1);
            } else {
                money.add(next);
            }
        }

        int sum = 0;
        for (Integer element : money) {
            sum += element;
        }
        bw.write(String.valueOf(sum));
        bw.flush();
        br.close();
        bw.close();
    }
}