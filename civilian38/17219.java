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

        HashMap<String, String> passwords = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int site = Integer.parseInt(st.nextToken());
        int pw = Integer.parseInt(st.nextToken());

        for (int i = 0; i < site; i++) {
            st = new StringTokenizer(br.readLine());
            String domain = st.nextToken();
            String password = st.nextToken();
            passwords.put(domain, password);
        }

        for (int i = 0; i < pw; i++) {
            bw.write(passwords.get(br.readLine()) + "\n");
        }


        bw.flush();
        br.close();
        bw.close();
    }

}