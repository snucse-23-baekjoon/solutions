import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main{
    public static boolean has_cord(HashMap<Integer, ArrayList<Integer>> cords, ArrayList<Integer> cord){
        if(cords.containsKey(cord.get(0))){
            return cords.get(cord.get(0)).contains(cord.get(1));
        }
        return false;
    }
    public static void dfs(HashMap<Integer, ArrayList<Integer>> cords, ArrayList<Integer> cord){
        cords.get(cord.get(0)).remove(cord.get(1));
        if (cords.get(cord.get(0)).isEmpty()){
            cords.remove(cord.get(0));
        }

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};
        for(int i = 0; i < 4; i++){
            ArrayList<Integer> ncord = new ArrayList<>();
            ncord.add(cord.get(0) + dx[i]);
            ncord.add(cord.get(1) + dy[i]);
            if(has_cord(cords, ncord)){
                dfs(cords, ncord);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int repeat = Integer.parseInt(br.readLine());
        for(int i = 0; i < repeat; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int col = Integer.parseInt(st.nextToken());
            int row = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            HashMap<Integer, ArrayList<Integer>> cords = new HashMap<>();
            for(int j = 0; j < n; j++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                if(!cords.containsKey(x)){
                    cords.put(x, new ArrayList<>());
                }
                cords.get(x).add(y);
            }

            int answer = 0;
            while(!cords.isEmpty()){
                ArrayList<Integer> ncord = new ArrayList<>();
                ncord.add(cords.keySet().iterator().next());
                ncord.add(cords.get(ncord.get(0)).get(0));

                dfs(cords, ncord);
                answer++;
            }
            bw.write(answer + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}