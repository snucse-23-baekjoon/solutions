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

        for(int i = 0; i < 3; i++){
            String line = br.readLine();
            if('0' <= line.charAt(0) && line.charAt(0) <= '9'){
                int number = Integer.parseInt(line) + 3 - i;
                if(number % 15 == 0){
                    bw.write("FizzBuzz");
                } else if  (number % 3 == 0){
                    bw.write("Fizz");
                } else if  (number % 5 == 0){
                    bw.write("Buzz");
                } else {
                    bw.write(String.valueOf(number));
                }
                break;
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}