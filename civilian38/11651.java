import java.io.BufferedWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main{
    public static ArrayList<int[]> merge(ArrayList<int[]> left, ArrayList<int[]> right){
        ArrayList<int[]> rtnList = new ArrayList<>();
        while (!left.isEmpty() && !right.isEmpty()){
            if (left.get(0)[1] < right.get(0)[1]){
                rtnList.add(left.remove(0));
            } else if (left.get(0)[1] > right.get(0)[1]){
                rtnList.add(right.remove(0));
            } else {
                if (left.get(0)[0] < right.get(0)[0]){
                    rtnList.add(left.remove(0));
                } else {
                    rtnList.add(right.remove(0));
                }
            }
        }
        rtnList.addAll(left);
        rtnList.addAll(right);
        return rtnList;
    }
    public static ArrayList<int[]> merge_sort(ArrayList<int[]> arr){
        if (arr.size() <= 1){
            return arr;
        } else {
            List<int[]> tempL = arr.subList(0, arr.size() / 2);
            ArrayList<int[]> left = new ArrayList<>(tempL);
            List<int[]> tempR = arr.subList(arr.size() / 2, arr.size());
            ArrayList<int[]> right = new ArrayList<>(tempR);
            return merge(merge_sort(left), merge_sort(right));
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int repeat = Integer.parseInt(br.readLine());
        ArrayList<int[]> arr = new ArrayList<>();

        for(int i = 0; i < repeat; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] cord  = new int[2];
            cord[0] = Integer.parseInt(st.nextToken());
            cord[1] = Integer.parseInt(st.nextToken());
            arr.add(cord);
        }

        ArrayList<int[]> merged_arr = merge_sort(arr);
        for(int[] cord: merged_arr){
            bw.write(String.valueOf(cord[0]) + " " + String.valueOf(cord[1]) + '\n');
        }

        bw.flush();
        br.close();
        bw.close();
    }
}