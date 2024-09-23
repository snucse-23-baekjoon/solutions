import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
    public static boolean isInBound(int[] cord, int sizeX, int sizeY){
        return (
                0 <= cord[0] &&
                cord[0] < sizeX &&
                0 <= cord[1] &&
                cord[1] < sizeY
                );
    }
    public static void rcc(int[][] distanceMap, int index, ArrayList<int[]> currentSearch){
        ArrayList<int[]> nextSearch = new ArrayList<>();

        for(int[] cord: currentSearch){
            int[] dx = {-1, 0, 1, 0};
            int[] dy = {0, -1, 0, 1};
            for(int i = 0; i < 4; i++){
                int[] tempCord = new int[]{cord[0] + dx[i], cord[1] + dy[i]};
                if(isInBound(tempCord, distanceMap.length, distanceMap[0].length) &&
                distanceMap[tempCord[0]][tempCord[1]] == -1
                ){
                    nextSearch.add(tempCord);
                    distanceMap[tempCord[0]][tempCord[1]] = index;
                }
            }
        }
        if(!nextSearch.isEmpty()){
            rcc(distanceMap, index + 1, nextSearch);
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int sizeX = Integer.parseInt(st.nextToken());
        int sizeY = Integer.parseInt(st.nextToken());
        int[][] map = new int[sizeX][sizeY];
        int[][] distanceMap = new int[sizeX][sizeY];
        int[] target = new int[]{-1, -1};
        for (int i = 0; i < sizeX; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < sizeY; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                distanceMap[i][j] = -1;
                if (map[i][j] == 2) {
                    target[0] = i;
                    target[1] = j;
                    distanceMap[i][j] = 0;
                } else if (map[i][j] == 0) {
                    distanceMap[i][j] = 0;
                }
            }
        }

        ArrayList<int[]> initial = new ArrayList<>();
        initial.add(new int[]{target[0], target[1]});
        rcc(distanceMap, 1, initial);

        for(int[] line: distanceMap){
            for(int dist: line){
                bw.write(String.valueOf(dist) + " ");
            }
            bw.write("\n");
        }


        bw.flush();
        br.close();
        bw.close();
    }
}