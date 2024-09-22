import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line = br.readLine();
        while (line != null) {
            if(line.charAt(0) == '.')
                break;
            boolean checker = true;
            int i = 0;
            Stack<Character> parentheses = new Stack<>();
            while (line.charAt(i) != '.'){
                if (line.charAt(i) == '(' || line.charAt(i) == '['){
                    parentheses.push(line.charAt(i));
                } else if (line.charAt(i) == ')'){
                    if(parentheses.isEmpty() || parentheses.pop() != '('){
                        checker = false;
                        break;
                    }
                } else if (line.charAt(i) == ']'){
                    if(parentheses.isEmpty() || parentheses.pop() != '['){
                        checker = false;
                        break;
                    }
                }
                i += 1;
            }
            if(!parentheses.isEmpty())
                checker = false;
            bw.write((checker ? "yes" : "no") + "\n");
            line = br.readLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}