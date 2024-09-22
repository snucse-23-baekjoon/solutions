import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int repeat = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> numbers = new HashMap<>();

        for (int i = 0; i < repeat; i++) {
            int number = Integer.parseInt(br.readLine());
            if(numbers.containsKey(number)) {
                numbers.put(number, numbers.get(number) + 1);
            } else {
                numbers.put(number, 1);
            }
        }

        for (int i = 1; i < 10001; i++){
            if(numbers.containsKey(i)) {
                bw.write((String.valueOf(i) + '\n').repeat(numbers.get(i)));
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}